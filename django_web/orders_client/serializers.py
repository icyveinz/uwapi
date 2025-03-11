from rest_framework import serializers
import re
from lexicon import rus


class CustomerSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    about_customer = serializers.CharField(max_length=1000)

    def validate_email(self, value):
        # Regular expression for validating a phone number with +, (), and -
        phone_regex = r"^\+?\d{1,3}?[-.\s]?\(?\d{2,4}?\)?[-.\s]?\d{2,4}[-.\s]?\d{2,4}[-.\s]?\d{0,4}$"

        # Regular expression for validating an email
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not (re.fullmatch(phone_regex, value) or re.fullmatch(email_regex, value)):
            raise serializers.ValidationError(rus['email_error'])

        return value
