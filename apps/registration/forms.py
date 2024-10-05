from django import forms
from .models import *



from django import forms

class LoginUserForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profile
        fields = ['username', 'password'] 


class UserRegister(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    p_number = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User   
        fields = ['username', 'password']   
        
class ItemRegister(forms.ModelForm):
    class Meta:
        model = ItemReg
        fields = '__all__'
        labels = {
            'item_name':'Name',
            'item_price':'Price Of the Item',
            'item_description':'Item details and description',
            'item_tag':'Tag_id',
            'item_type':'Type',         
        }