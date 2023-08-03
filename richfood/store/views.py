from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    banners = Banner.objects.all()[:2]
    banners1 = Banner.objects.all()[2:11]


    context ={
        'banners':banners,
        'banners1':banners1
    }
    return render(request, 'store/index.html',context)
    