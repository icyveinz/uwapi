# Create your views here.
import asyncio
import sentry_sdk
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from lexicon import rus
from nats_publisher.client import send_message
from orders_client.models import Order
from orders_client.serializers import CustomerSerializer


class CustomerCreateView(APIView):
    def post(self, request, parent: str):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer_data = serializer.validated_data
            try:
                if parent == "ugo" or parent == "wgl":
                    order = Order.objects.create(
                        parent=parent.upper(),
                        status="Не обработан",
                        customer_name=customer_data["name"],
                        customer_email=customer_data["email"],
                        customer_description=customer_data["about_customer"],
                    )

                    asyncio.run(send_message("new.customer", model_to_dict(order)))

                    return Response(
                        {"is_succeed": True, "message": rus["template_success"]},
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        {"is_succeed": False, "message": rus["src_error"]},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            except Exception as e:
                sentry_sdk.capture_exception(e)
                return Response(
                    {"is_succeed": False, "message": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(
            {"is_succeed": False, "message": rus["data_error"]},
            status=status.HTTP_400_BAD_REQUEST,
        )
