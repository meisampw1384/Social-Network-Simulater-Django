from django.db import models
from django.conf import settings


class Country(models.Model):
    name=models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    is_active=models.BooleanField(default=True)
    created_time= models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Country'
        verbose_name_plural = 'Countries'
        #db_table = 'countries
    
class Profile(models.Model):
    user = models.OneToOneField(to = settings.AUTH_USER_MODEL , on_delete= models.CASCADE)
    phone_number = models.BigIntegerField(blank = True, null = True , unique=True)
    Country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    avatar= models.ImageField(blank = True)