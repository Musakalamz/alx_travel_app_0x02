from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'listings', views.ListingViewSet, basename='listing')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('', include(router.urls)),
    path('payments/initiate/', views.initiate_payment, name='initiate_payment'),
    path('payments/verify/', views.verify_payment, name='verify_payment'),
]
