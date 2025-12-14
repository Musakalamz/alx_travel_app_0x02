from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Payment

@shared_task
def send_payment_confirmation(payment_id: int):
    try:
        payment = Payment.objects.select_related('booking', 'booking__listing', 'booking__user').get(id=payment_id)
    except Payment.DoesNotExist:
        return
    recipient = payment.customer_email or (payment.booking.user.email if payment.booking.user else None)
    if not recipient:
        return
    subject = "Payment Confirmation - ALX Travel App"
    message = (
        f"Your payment with reference {payment.tx_ref} has been confirmed.\n"
        f"Booking: {payment.booking.listing.title}\n"
        f"Amount: {payment.amount} {payment.currency}\n"
        f"Status: {payment.status}\n"
    )
    send_mail(subject, message, settings.EMAIL_HOST_USER or "no-reply@alxtravelapp.local", [recipient], fail_silently=True)
