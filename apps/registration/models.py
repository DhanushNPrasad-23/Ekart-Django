from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Profile')
    p_number = models.CharField(max_length=10,null=True,blank=True)
    

    
    
    def __str__(self):
        return self.user.username
    

class ItemReg(models.Model):
    
    itemtype = [('','select the choice'),
                ('F','Fashion'),
                ('A','Appliances'),
                ('G','grocerys')]
    
    item_name = models.CharField(max_length=50)
    item_price = models.BigIntegerField()
    item_description = models.TextField(max_length=500,null=True,blank=True)
    item_tag = models.CharField(max_length=10,unique=True)
    item_type = models.CharField(max_length=10, choices=itemtype,null=True,blank=True)
    item_image = models.ImageField(upload_to='images',blank=True,null=True)
    
    def __str__(self) -> str:
        return self.item_name
    
    
