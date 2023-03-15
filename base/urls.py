from django.urls import path

from .views import (
    CreateDustbinAPIView,
    CreateDustbinGroupAPIView,
    EditDustbinAPIView,
    EditUserAPIView,
    ListDustbinGroupAPIView,
    ListUserAPIView,
    LoginAPIView,
    RegisterAPIView,
    ListDustbinsAPIView,
    AddDustbinToGroupAPIView,
    DeleteDustbinFromGroupAPIView,
    EditDustbinGroupAPIView,
)

urlpatterns = [
    path("api/register/", RegisterAPIView.as_view(), name="register"),
    path("api/login/", LoginAPIView.as_view(), name="login"),
    path("api/create-dustbin/", CreateDustbinAPIView.as_view(), name="create-dustbin"),
    path(
        "api/create-dustbin-group/",
        CreateDustbinGroupAPIView.as_view(),
        name="create-group",
    ),
    path(
        "api/add-dustbin-to-group/<int:pk>",
        AddDustbinToGroupAPIView.as_view(),
        name="add-dustbin-to-group",
    ),
    path(
        "api/delete-dustbin-from-group/<int:pk>",
        DeleteDustbinFromGroupAPIView.as_view(),
        name="delete-dustbin-from-group",
    ),
    path("api/user-edit/", EditUserAPIView.as_view(), name="edit-user"),
    path("api/dustbin-edit/", EditDustbinAPIView.as_view(), name="edit-dustbin"),
    path(
        "api/dustbin-group-edit/",
        EditDustbinGroupAPIView.as_view(),
        name="edit-dustbin-group",
    ),
    path("api/list-dustbins/", ListDustbinsAPIView.as_view(), name="list-dustbins"),
    path("api/list-users/", ListUserAPIView.as_view(), name="list-users"),
    path("api/list-groups/", ListDustbinGroupAPIView.as_view(), name="list-groups"),
]
