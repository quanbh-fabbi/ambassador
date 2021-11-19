from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('common.urls')),
    path('products/frontend', ProductFrontEndAPIView.as_view()),
    path('products/backend', ProductBackEndAPIView.as_view()),
    path('links', LinkAPIView.as_view()),
]
