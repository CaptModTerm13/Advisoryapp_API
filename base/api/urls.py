from django.urls import path
from .views import UserView,UserProfileView,UpdateUser

urlpatterns=[
    path("",UserView.as_view(),name="usersList"),
    path("user/<username>", UserProfileView.as_view(), name="user_detail"),
    path("update/<username>",UpdateUser.as_view(),name="update-view")
]