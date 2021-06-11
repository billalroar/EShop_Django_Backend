from django.shortcuts import render
from eShopReact.models import customer
from eShopReact.serializer import CustomerSerializer
from eShopReact.models.customer import Customer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class CustomerAPIView(APIView):
    serializer_calss = CustomerSerializer

    def get_queryset(self):
        customer =  Customer.objects.all()
        return customer
    
    def post(self,request,*args,**kwargs):
        data = request.data
        error=False
        message=''
        print(request.data.get("email"))
        customer_have = Customer.objects.filter(email=data['email']).exists();
        if customer_have:
            error=True
            message='This Email Already exists'
            print(error)
        else:
            new_customer = Customer.objects.create(first_name = data["first_name"],last_name=data["last_name"],
            phone=data['phone'],email=data['email'],password=data['password'],address=data['address'],
            city=data['city'],state=data['state'],zip=data['zip']);
            new_customer.save()
            error=False
            message='successful'
            print(error)

        return Response({'error':error,"message":message})