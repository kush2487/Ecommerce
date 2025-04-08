from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from products.models import Products
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

# # Create your views here. 
def changing_api(request):
    data = Products.objects.all()
    d = data[0]
    d.name = 'testing_124'
    d.save()
    data = Products.objects.all()
    print(data)
    return HttpResponse(data)


@api_view(['GET'])
def get_products(request):
    data = Products.objects.all()
    serializerProducts = ProductSerializer(data, many = True)
    return Response(serializerProducts.data)


@api_view(['GET'])
def get_products_id(request, id):
    try:
        data = Products.objects.get(id = id )
        serializerProducts = ProductSerializer(data)
        return Response(serializerProducts.data)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def creating_product(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



@api_view(['PATCH'])
def update_product(request, id):
    try:
        product = Products.objects.get(id = id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product, data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_product_full(request, id):
    try:
        product = Products.objects.get(id = id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product(request, id):
    try:
        product = Products.objects.get(id = id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    product.delete()
    return Response({"message": "Product Deleted Sucessfully"}, status=status.HTTP_204_NO_CONTENT)
    