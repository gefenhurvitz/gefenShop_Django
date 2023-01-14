from django.http import JsonResponse
from .products import products

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
 



def index(req):
    return JsonResponse('hello', safe=False)

@api_view(['GET'])
def getProducts(req):
    return Response(products)
