from django.db import models

# Create your models here.

class Banner(models.Model):
    name  = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='BannerImage')
    
    class Meta:
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.name
