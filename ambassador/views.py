from rest_framework.response import Response
from rest_framework.views import APIView

from administrator.serializers import ProductSerializer
from core.models import Product


class ProductFrontEndAPIView(APIView):

    def get(self, _):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductBackEndAPIView(APIView):

    def get(self, _):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
