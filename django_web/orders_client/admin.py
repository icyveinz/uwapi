# Register your models here.
from django.contrib import admin
from lexicon import rus
from orders_client.models import Order, Comment, Photo


@admin.action(description=rus["actions"]["declined"])
def mark_as_declined(modeladmin, request, queryset):
    queryset.update(status=rus["models"]["order"]["status_choices"]["declined"])


@admin.action(description=rus["actions"]["in_process"])
def mark_in_progress(modeladmin, request, queryset):
    queryset.update(status=rus["models"]["order"]["status_choices"]["in_process"])


@admin.action(description=rus["actions"]["as_completed"])
def mark_as_completed(modeladmin, request, queryset):
    queryset.update(status=rus["models"]["order"]["status_choices"]["completed"])


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
    search_fields = ["customer_name", "customer_email", "customer_description"]
    list_filter = [
        "status",
        "parent",
        ("timestamp", admin.DateFieldListFilter),
    ]
    list_editable = ["status"]
    inlines = [CommentInline]
    actions = [mark_as_declined, mark_in_progress, mark_as_completed]

    def comments_count(self, obj):
        return obj.comments.count()

    comments_count.short_description = "Комментарии"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "uploaded_at", "image")


admin.site.register(Order, OrderAdmin)
admin.site.register(Comment)
