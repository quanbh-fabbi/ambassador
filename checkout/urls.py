from django.urls import path
from .views import *

urlpatterns = [
    path('link/<str:code>', LinkAPIView.as_view())
]