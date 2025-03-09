from django.db import models

from lexicon import rus


class Order(models.Model):
    STATUS_CHOICES = [
        (
            rus["models"]["order"]["status_choices"]["unseen"],
            rus["models"]["order"]["status_choices"]["unseen"],
        ),
        (
            rus["models"]["order"]["status_choices"]["declined"],
            rus["models"]["order"]["status_choices"]["declined"],
        ),
        (
            rus["models"]["order"]["status_choices"]["in_process"],
            rus["models"]["order"]["status_choices"]["in_process"],
        ),
        (
            rus["models"]["order"]["status_choices"]["completed"],
            rus["models"]["order"]["status_choices"]["completed"],
        ),
    ]

    PARENT_CHOICES = [
        (
            rus["models"]["order"]["parent_choices"]["ugo"],
            rus["models"]["order"]["parent_choices"]["ugo"],
        ),
        (
            rus["models"]["order"]["parent_choices"]["wgl"],
            rus["models"]["order"]["parent_choices"]["wgl"],
        ),
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

    @property
    def comments_count(self):
        return self.comments.all().count()


class Comment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Комментарий к заказу {self.order.id}"
