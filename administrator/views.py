from django.shortcuts import render

from common.serializers import UserSerializer
from core.models import *
from rest_framework.views import APIView
from rest_framework.response import Response


class AmbassadorAPIView(APIView):
    def get(self, _):
        ambassador = User.objects.filter(is_ambassador=True)
        serializer = UserSerializer(ambassador, many=True)
        return Response(serializer.data)