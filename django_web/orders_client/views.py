# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from lexicon import rus
from orders_client.models import Order
from orders_client.serializers import CustomerSerializer


class CustomerCreateView(APIView):
    def post(self, request, parent : str):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer_data = serializer.validated_data
            try:
                if parent == "ugo" or parent == "wgl":
                    Order.objects.create(
                        parent=parent.upper(),
                        status="Не обработан",
                        customer_name=customer_data['name'],
                        customer_email=customer_data['email'],
                        customer_description=customer_data['about_customer']
                    )
                    return Response({
                        "is_succeed": True,
                        "message": rus['template_success']
                    }, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        "is_succeed": False,
                        "message": rus['src_error']
                    }, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                return Response({
                    "is_succeed": False,
                    "message": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "is_succeed": False,
            "message": rus['data_error']
        }, status=status.HTTP_400_BAD_REQUEST)