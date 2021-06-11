from django.shortcuts import render
from eShopReact.models import product
from eShopReact.serializer import OrderSerializer
from eShopReact.models.orders import Order
from rest_framework.views import APIView
from rest_framework.response import Response
from eShopReact.models.customer import Customer
from eShopReact.models.product import Product

# Create your views here.

class OrderAPIView(APIView):
    serializer_calss = OrderSerializer

    def get_queryset(self):
        customer =  Order.objects.all()
        return customer

    def get(self,request,*args,**kwargs):
        data = request.query_params['id']
        error=False
        message=''
        try:
            error = False
            customerId = Customer.objects.get(id=data)
            product = Order.objects.filter(customer=customerId)
            print(product)
            serializer = OrderSerializer(product,context={'request':request},many=True)
            return Response({'error':error,"message":'',"result":serializer.data})
        except:
            error=True
            message='Server Error'
            return Response({'error':error,"message":message,"result":''})
    
    def post(self,request,*args,**kwargs):
        data = request.data
        error=False
        message=''
        try:
            cart= data['cart']
            id = data['user_id']
            userId = Customer.objects.get(id=id['id'])
            for k in cart.keys():
                productId = Product.objects.get(id=k)
                o= Order.objects.create(product=productId,customer=userId,quantity=cart[k]['quantity'],price=cart[k]['price'])
            error=False
            message='Order Successful '
            return Response({'error':error,"message":message})
        except:
            error=True
            message='Server Error'
            return Response({'error':error,"message":message})
        