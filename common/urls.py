from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('user', UserAPIView.as_view()),

]
