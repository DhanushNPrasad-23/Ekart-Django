from django.db import models

# Create your models here.


class Base1(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class Base2(Base1):
    age = models.IntegerField(null=True,default=20)
    last_name = models.CharField(max_length=100,null=True,default=None)
    
    
    def __str__(self) -> str:
        return self.name
    