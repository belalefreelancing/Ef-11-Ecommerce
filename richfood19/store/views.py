from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    banners = Banner.objects.all()[:2]
    banners1 = Banner.objects.all()[2:11]
    categories = Category.objects.all()
    products = Product.objects.all()

    context ={
        'banners':banners,
        'banners1':banners1,
        'categories':categories,
        'products':products
    }
    return render(request, 'store/index.html',context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product':product
    }
    return render(request, 'store/product-detail.html', context)
    
    