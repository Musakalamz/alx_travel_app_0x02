from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer
from drf_yasg.utils import swagger_auto_schema
import requests
import uuid
from django.utils import timezone

@swagger_auto_schema(
    method='get',
    operation_description="Welcome endpoint for ALX Travel App API"
)
@api_view(['GET'])
def welcome_view(request):
    """Welcome endpoint for the ALX Travel App API"""
    return Response({
        "message": "Welcome to ALX Travel App API",
        "status": "success"
    })

class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.select_related("listing").all()
    serializer_class = BookingSerializer
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        booking_id = response.data.get('id')
        try:
            booking = Booking.objects.select_related('listing').get(id=booking_id)
        except Booking.DoesNotExist:
            return response
        tx_ref = f"booking-{booking.id}-{uuid.uuid4().hex[:12]}"
        currency = request.data.get('currency') or 'ETB'
        email = request.data.get('email') or (booking.user.email if booking.user and booking.user.email else '')
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        initialize_url = f"{settings.CHAPA_BASE_URL}/v1/transaction/initialize"
        headers = {'Authorization': f"Bearer {settings.CHAPA_SECRET_KEY}"}
        payload = {
            'amount': str(booking.total_price),
            'currency': currency,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'tx_ref': tx_ref,
            'callback_url': settings.PAYMENT_RETURN_URL,
            'return_url': settings.PAYMENT_RETURN_URL,
        }
        try:
            resp = requests.post(initialize_url, json=payload, headers=headers, timeout=20)
            data = resp.json()
            if resp.status_code == 200 and data.get('status') == 'success':
                checkout_url = data.get('data', {}).get('checkout_url')
                chapa_txn_id = data.get('data', {}).get('tx_ref') or tx_ref
                Payment.objects.create(
                    booking=booking,
                    tx_ref=tx_ref,
                    chapa_transaction_id=chapa_txn_id,
                    status=Payment.Status.PENDING,
                    amount=booking.total_price,
                    currency=currency,
                    customer_email=email,
                    checkout_url=checkout_url
                )
                response.data['payment_checkout_url'] = checkout_url
                response.data['payment_tx_ref'] = tx_ref
        except Exception:
            pass
        return response

@api_view(['POST'])
def initiate_payment(request):
    booking_id = request.data.get('booking_id')
    currency = request.data.get('currency') or 'ETB'
    email = request.data.get('email')
    first_name = request.data.get('first_name', '')
    last_name = request.data.get('last_name', '')
    if not booking_id:
        return Response({'detail': 'booking_id is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        booking = Booking.objects.select_related('listing').get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({'detail': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
    tx_ref = f"booking-{booking.id}-{uuid.uuid4().hex[:12]}"
    amount = str(booking.total_price)
    initialize_url = f"{settings.CHAPA_BASE_URL}/v1/transaction/initialize"
    headers = {'Authorization': f"Bearer {settings.CHAPA_SECRET_KEY}"}
    payload = {
        'amount': amount,
        'currency': currency,
        'email': email or (booking.user.email if booking.user and booking.user.email else ''),
        'first_name': first_name or (booking.user.first_name if booking.user else ''),
        'last_name': last_name or (booking.user.last_name if booking.user else ''),
        'tx_ref': tx_ref,
        'callback_url': settings.PAYMENT_RETURN_URL,
        'return_url': settings.PAYMENT_RETURN_URL,
    }
    try:
        resp = requests.post(initialize_url, json=payload, headers=headers, timeout=20)
        data = resp.json()
    except Exception as e:
        return Response({'detail': 'Payment initialization failed'}, status=status.HTTP_502_BAD_GATEWAY)
    if resp.status_code != 200 or data.get('status') != 'success':
        return Response({'detail': 'Payment initialization error', 'data': data}, status=status.HTTP_400_BAD_REQUEST)
    checkout_url = data.get('data', {}).get('checkout_url')
    chapa_txn_id = data.get('data', {}).get('tx_ref') or tx_ref
    payment = Payment.objects.create(
        booking=booking,
        tx_ref=tx_ref,
        chapa_transaction_id=chapa_txn_id,
        status=Payment.Status.PENDING,
        amount=booking.total_price,
        currency=currency,
        customer_email=email or (booking.user.email if booking.user and booking.user.email else ''),
        checkout_url=checkout_url
    )
    return Response({'checkout_url': checkout_url, 'tx_ref': tx_ref, 'payment_id': payment.id}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def verify_payment(request):
    tx_ref = request.query_params.get('tx_ref')
    if not tx_ref:
        return Response({'detail': 'tx_ref is required'}, status=status.HTTP_400_BAD_REQUEST)
    verify_url = f"{settings.CHAPA_BASE_URL}/v1/transaction/verify/{tx_ref}"
    headers = {'Authorization': f"Bearer {settings.CHAPA_SECRET_KEY}"}
    try:
        resp = requests.get(verify_url, headers=headers, timeout=20)
        data = resp.json()
    except Exception:
        return Response({'detail': 'Payment verification failed'}, status=status.HTTP_502_BAD_GATEWAY)
    try:
        payment = Payment.objects.select_related('booking').get(tx_ref=tx_ref)
    except Payment.DoesNotExist:
        return Response({'detail': 'Payment record not found'}, status=status.HTTP_404_NOT_FOUND)
    is_success = resp.status_code == 200 and data.get('status') == 'success' and data.get('data', {}).get('status') == 'success'
    if is_success:
        payment.status = Payment.Status.COMPLETED
        payment.save(update_fields=['status', 'updated_at'])
        booking = payment.booking
        booking.status = Booking.Status.CONFIRMED
        booking.save(update_fields=['status'])
        try:
            from .tasks import send_payment_confirmation
            send_payment_confirmation.delay(payment.id)
        except Exception:
            pass
        return Response({'status': 'COMPLETED', 'tx_ref': tx_ref}, status=status.HTTP_200_OK)
    payment.status = Payment.Status.FAILED
    payment.save(update_fields=['status', 'updated_at'])
    return Response({'status': 'FAILED', 'tx_ref': tx_ref, 'data': data}, status=status.HTTP_400_BAD_REQUEST)
