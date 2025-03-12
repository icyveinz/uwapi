from django.urls import path
from .views import CustomerCreateView, ReleaseImagesForWidget

urlpatterns = [
    path("create/<str:parent>/", CustomerCreateView.as_view(), name="create_order"),
    path("get_images/", ReleaseImagesForWidget.as_view(), name="get_images"),
]
