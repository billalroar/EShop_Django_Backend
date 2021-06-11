from django.shortcuts import render
from eShopReact.serializer import CategorySerializer
from eShopReact.models.category import Category
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class CategoryAPIView(APIView):
    serializer_calss = CategorySerializer

    def get_queryset(self):
        category =  Category.objects.all()
        return category
    
    def get(self,request,*args,**kwargs):

        
        category = self.get_queryset()
        serializer = CategorySerializer(category,many=True)
        
        return Response(serializer.data)