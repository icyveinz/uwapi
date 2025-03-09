from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ("Не обработан", "Не обработан"),
        ("Отказ", "Отказ"),
        ("В процессе", "В процессе"),
        ("Завершен", "Завершен"),
    ]

    PARENT_CHOICES = [
        ("UGO", "UGO"),
        ("WGL", "WGL"),
    ]

    id = models.AutoField(primary_key=True)
    parent = models.CharField(max_length=50, choices=PARENT_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    customer_name = models.TextField()
    customer_email = models.EmailField()
    customer_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"Order {self.id} - {self.status}"


class Comment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Комментарий к заказу {self.order.id}"
