from django.urls import path
from .views import CustomerCreateView

urlpatterns = [
    path('create/<str:parent>/', CustomerCreateView.as_view(), name='create_order'),
]