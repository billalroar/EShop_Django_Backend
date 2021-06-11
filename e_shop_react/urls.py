"""e_shop_react URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings
from eShopReact.views.ProductView import ProductsAPIView
from eShopReact.views.catagory import CategoryAPIView
from eShopReact.views.ProductViewbyId import ProductViewbyIdAPIView
from eShopReact.views.coustomer import CustomerAPIView
from eShopReact.views.login import LoginAPIView
from eShopReact.views.order import OrderAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductsAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
    path('productbyId/', ProductViewbyIdAPIView.as_view()),
    path('customer/', CustomerAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('order/', OrderAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
