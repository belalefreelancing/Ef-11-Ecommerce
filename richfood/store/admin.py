from django.contrib import admin
from .models import *
# Register your models here.

my_models = [Banner,Category,Brand,Product,ProductRelatedImage]

admin.site.register(my_models)