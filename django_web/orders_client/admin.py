# Register your models here.
from django.contrib import admin
from orders_client.models import Order, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ("comment", "created_at")
    readonly_fields = ["created_at"]


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "parent",
        "status",
        "customer_name",
        "customer_email",
        "customer_description",
        "comments_count",
        "timestamp",
    )
    list_per_page = 10
    search_fields = ["customer_name", "customer_email"]
    list_filter = ["status", "parent"]
    list_editable = ["status"]
    inlines = [CommentInline]

    def comments_count(self, obj):
        return obj.comments.count()

    comments_count.short_description = "Comments"


admin.site.register(Order, OrderAdmin)
admin.site.register(Comment)
