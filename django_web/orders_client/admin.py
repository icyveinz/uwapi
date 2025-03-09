# Register your models here.
from django.contrib import admin
from orders_client.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "status",
        "customer_email",
        "customer_description",
        "timestamp",
    )
    search_fields = ["customer_name", "customer_email"]
    list_filter = ["status", "parent"]
    list_editable = ["status"]  # Делаем статус редактируемым


admin.site.register(Order, OrderAdmin)
