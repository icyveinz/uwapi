from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=255)
    about_customer = serializers.CharField(max_length=1000)
