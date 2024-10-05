from django.db import models
from django.contrib.auth.models import User
from apps.registration.models import *
# Create your models here.

class OrderHistory(models.Model):
    item = models.OneToOneField(ItemReg,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class History(models.Model):
    item = models.ForeignKey(ItemReg, on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    order_date = models.DateTimeField(auto_now_add=True) 
    quantity = models.PositiveIntegerField(default=1)  
    status = models.CharField(
        max_length=20, 
        choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')],
        default='Pending'
    ) 
    def __str__(self):
        return f"{self.user.username} - {self.item.item_name} - {self.order_date}"