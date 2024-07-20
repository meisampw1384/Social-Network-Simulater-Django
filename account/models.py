from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


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
    user = models.OneToOneField(to = settings.AUTH_USER_MODEL , on_delete= models.CASCADE,related_name='profile')
    phone_number = models.BigIntegerField(blank = True, null = True , unique=True)
    Country = models.ForeignKey(to=Country, on_delete=models.CASCADE,null=True , blank = True)
    avatar= models.ImageField(blank = True)
    
class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2 
    DEVICE_ANDROID = 3
    DEVICE_PC =4 
    DEVICE_TYPE_CHOICES= ((1,'web'),
                          (2,'ios'),
                          (3,'android'),
                          (4,'pc'))
    
    user = models.ForeignKey(to=User,related_name='devices',on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device UUID',null=True)
    last_login = models.DateTimeField('last login date',null = True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES,default=DEVICE_WEB)
    device_os = models.CharField('device os',max_length=20,blank=True)
    device_model=models.CharField('device model',max_length=20,blank=True)
    app_version = models.CharField('app version',max_length=20,blank = True)
    
    class Meta:
        db_table='user_devices'
        verbose_name = _('device')
        verbose_name_plural=_('devices')
        unique_together=('user','device_uuid')