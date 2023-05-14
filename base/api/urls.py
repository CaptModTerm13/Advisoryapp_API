from django.urls import path
from .views import UserView,UserProfileView

urlpatterns=[
    path("",UserView.as_view(),name="usersList"),
    path("user/<username>", UserProfileView.as_view(), name="user_detail"),
    
]