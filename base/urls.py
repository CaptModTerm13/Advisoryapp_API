from django.urls import path
from .views import index,success,get_name
from allauth.account.views import LoginView

urlpatterns=[
    path("",index),
    path("login",LoginView.as_view(),),
    path("home",get_name,name="homepage"),
    path("sucess",success)
  

  

  
    
]