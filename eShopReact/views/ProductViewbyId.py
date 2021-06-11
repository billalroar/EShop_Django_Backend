from os import name
from eShopReact.models.category import Category
from django.shortcuts import render
from eShopReact.serializer import ProductsSerializer
from eShopReact.models.product import Product
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProductViewbyIdAPIView(APIView):
    serializer_calss = ProductsSerializer

    def get_queryset(self):
        product =  Product.objects.all()
        return product
    
    def get(self,request,*args,**kwargs):
            productId = request.query_params['productid']
            p=productId.split(',')
            # data = request.data
            if p != None :
                product = Product.get_product_by_id(p)
                print(product)
                serializer = ProductsSerializer(product,context={'request':request},many=True)
            
       
            return Response(serializer.data)