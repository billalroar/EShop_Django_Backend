from django.shortcuts import render
from eShopReact.models import customer
from eShopReact.serializer import CustomerSerializer
from eShopReact.models.customer import Customer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class LoginAPIView(APIView):
    serializer_calss = CustomerSerializer

    def get_queryset(self):
        customer =  Customer.objects.all()
        return customer
    
    def post(self,request,*args,**kwargs):
        data = request.data
        error=False
        message=''
        customer = Customer.objects.filter(email=data['email'],password=data['password'])
        print(customer)
        if not customer:
            error=True
            message='Email or Password is incorrect !!!'
            return Response({'error':error,"message":message,'data':''})
        else:
            error=False
            message='successful'
            print(error)
            serializer = CustomerSerializer(customer,many=True)
            return Response({'error':error,"message":message,'data':serializer.data})