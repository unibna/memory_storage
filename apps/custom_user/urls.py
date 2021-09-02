from django.urls import path 
from django.contrib.auth.views import LogoutView

from .views import CustomLoginView, CustomRegisterView


urlpatterns = [ 
    path('register', CustomRegisterView.as_view(), name='register'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]