# Register your models here.
from django.contrib import admin
from orders_client.models import Order, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ("comment", "created_at")
    readonly_fields = ["created_at"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ( "parent", "status", "customer_name", "customer_email", "customer_description", "timestamp")
    search_fields = ["customer_name", "customer_email"]
    list_filter = ["status", "parent"]
    list_editable = ["status"]  # Делаем статус редактируемым
    inlines = [CommentInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Comment)
