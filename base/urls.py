from django.urls import path
from .views import index,homepage
from allauth.account.views import LoginView

urlpatterns=[
    path("",LoginView.as_view(),),
    path("home",homepage,name="homepage")
  
    
]