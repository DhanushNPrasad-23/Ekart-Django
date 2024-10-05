from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CartItems(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    item_tag = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.item_tag
    