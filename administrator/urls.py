from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('common.urls')),
    path('ambassadors', AmbassadorAPIView.as_view()),
    path('products', ProductGenericAPIView.as_view()),
    path('products/<str:pk>', ProductGenericAPIView.as_view()),
    path('users/<str:pk>/link', LinkAPIView.as_view()),
]
