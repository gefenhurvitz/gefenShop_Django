from django.http import JsonResponse
from .products import products
 
def index(req):
    return JsonResponse('hello', safe=False)


def getProducts(req):
    return JsonResponse(products, safe=False)
