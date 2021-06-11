from os import name
from eShopReact.models.category import Category
from django.shortcuts import render
from eShopReact.serializer import ProductsSerializer
from eShopReact.models.product import Product
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProductsAPIView(APIView):
    serializer_calss = ProductsSerializer

    def get_queryset(self):
        product =  Product.objects.all()
        return product
    
    def get(self,request,*args,**kwargs):
        # categoryName = request.query_params['categoryName']
        # print(categoryName)
        try:
            categoryName = request.query_params['categoryName']

            # data = request.data
            print(categoryName)
            if categoryName != None :
                categoryId = Category.objects.get(name=categoryName)
                product = Product.objects.filter(category=categoryId)
                serializer = ProductsSerializer(product,context={'request':request},many=True)
        except:
            products = self.get_queryset()
            print(products)
            serializer = ProductsSerializer(products,context={'request':request},many=True)
        
        return Response(serializer.data)