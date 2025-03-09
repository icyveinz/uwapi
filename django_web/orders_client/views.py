# Create your views here.
from rest_framework.views import APIView
from orders_client.models import Order
from orders_client.serializers import CustomerSerializer


class CustomerCreateView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer_data = serializer.validated_data

            Order.objects.create(
                parent="UGO",
                status="Не обработан",
                customer_name=customer_data['name'],
                customer_email=customer_data['email'],
                customer_description=customer_data['about_customer']
            )

            return Response({
                "is_succeed": True,
                "message" : "Ваш запрос был отправлен! Мы свяжемся с вами как можно скорее."
            })