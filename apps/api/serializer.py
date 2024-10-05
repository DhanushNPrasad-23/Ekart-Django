from rest_framework import serializers
from .models import *



class BaseSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Base2
        fields = '__all__'

class BaseOne(serializers.ModelSerializer):
    class Meta:
        model = Base2
        fields = ['name','last_name']
        