from django.db import models
from django.contrib.auth.models import User
from apps.registration.models import ItemReg
# Create your models here.


class Buy(models.Model):
    
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    email  = models.EmailField(null=True,blank=True)
    address = models.TextField(max_length=250)
    
    def __str__(self) -> str:
        return self.phone_number  
    
class Order(models.Model):
    choice_order = [
        ('','Select the catagaroies'),
        ('P','Pending'),
        ('C','Completed'),
        ('F','Failed')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    item = models.OneToOneField(ItemReg,on_delete=models.CASCADE)
    order_item_id = models.CharField(max_length=10)
    order_details = models.OneToOneField(Buy,on_delete=models.CASCADE)
    order_status = models.CharField(max_length=10,choices=choice_order,default='P',null=True,blank=True)
    
    def __str__(self) -> str:
        return self.order_item_id
    