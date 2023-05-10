from django.urls import path
from .views import UserView,UserProfileView,UpdateUser

urlpatterns=[
    path("",UserView.as_view(),name="users"),
    path("user/<username>", UserProfileView.as_view(), name="post_detail"),
    path("update/<username>",UpdateUser.as_view(),name="update-view")
]