# Register your models here.
from django.contrib import admin
from orders_client.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "customer_email",
        "status",
        "timestamp",
    )  # Fields to display in list view
    search_fields = [
        "customer_name",
        "customer_email",
    ]  # Enable search by customer_name or customer_email
    list_filter = ["status"]  # Add filters for status field


admin.site.register(Order, OrderAdmin)
