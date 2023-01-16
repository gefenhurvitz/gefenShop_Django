from django.http import JsonResponse

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
 
# import product model
from .models import Product

# import serializers
from .serializers import ProductSerializer


def index(req):
    return JsonResponse('hello', safe=False)

@api_view(['GET'])
def getProducts(req):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getProduct(req, pk):
    product = Product.objects.get(_id = pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)