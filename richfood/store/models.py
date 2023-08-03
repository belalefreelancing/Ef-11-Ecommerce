from django.db import models

# Create your models here.

class Banner(models.Model):
    name  = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='BannerImage')
    
    class Meta:
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.name



class Category(models.Model):
    image = models.ImageField(upload_to='CategoryImage')
    name = models.CharField(max_length = 150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='BrandImage')

    def __str__(self):
        return self.name


class Product(models.Model):
    name  = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ProductImage')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand  = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock_quantity  = models.IntegerField()
    

    def __str__(self):
        return self.name
        

class ProductRelatedImage(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ProductImage')
    
    
    def __str__(self):
        return self.product.name
    
    
    
