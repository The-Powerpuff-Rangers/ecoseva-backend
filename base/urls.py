from django.urls import path

from .views import LoginAPIView, RegisterAPIView, EditUserAPIView

urlpatterns = [
    path("api/register/", RegisterAPIView.as_view(), name="register"),
    path("api/login/", LoginAPIView.as_view(), name="login"),
    path("api/edit/", EditUserAPIView.as_view(), name="edit"),
]
