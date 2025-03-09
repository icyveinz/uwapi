# Register your models here.
from django.contrib import admin
from orders_client.models import Order, Comment


@admin.action(description="Установить 'Отказ' для выбранных")
def mark_as_declined(modeladmin, request, queryset):
    queryset.update(status="Отказ")


@admin.action(description="Установить 'В процессе' для выбранных")
def mark_in_progress(modeladmin, request, queryset):
    queryset.update(status="В процессе")


@admin.action(description="Установить 'Завершен' для выбранных")
def mark_as_completed(modeladmin, request, queryset):
    queryset.update(status="Завершен")


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
    actions = [mark_as_declined, mark_in_progress, mark_as_completed]

    def comments_count(self, obj):
        return obj.comments.count()

    comments_count.short_description = "Comments"


admin.site.register(Order, OrderAdmin)
admin.site.register(Comment)
