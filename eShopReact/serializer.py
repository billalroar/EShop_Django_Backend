from e_shop_react import settings
from .models.category import Category
from .models.customer import Customer
from .models.product import Product
from .models.orders import Order
from rest_framework  import fields, serializers

from eShopReact.models import orders

class ProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id','name','category','price','image']
        depth = 1 # for forigen key data show

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url =obj.fingerprint.url
        return request.build_absolute_uri(photo_url)


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        depth = 1 # for forigen key data show

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1 # for forigen key data show

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        depth = 1 # for forigen key data show
    
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url =obj.fingerprint.url
        return request.build_absolute_uri(photo_url)



    