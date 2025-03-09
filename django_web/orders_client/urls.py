from django.urls import path
from .views import CustomerCreateView

urlpatterns = [
    path('api/orders/ugo', CustomerCreateView.as_view(), name='create_order'),
]