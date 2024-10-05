from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from apps.registration.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import CartItems
from django.db.models import F, OuterRef, Subquery
from django.contrib import messages
from apps.registration.models import ItemReg

# Create your views here.
@login_required(login_url='login')
def cart_view(request):
    user = User.objects.get(username=request.user.username)
    
    result = CartItems.objects.filter(username=user)
    
    item_tags = result.values_list('item_tag', flat=True)
    
    
    res = ItemReg.objects.filter(id__in=item_tags)
    
    
    
    return render(request, 'cart_view.html', {'res': res})

@login_required(login_url='login')
def cart_add_item(request,item_id):
    user = request.user
    item_id = str(item_id)
    
    CartItems.objects.create(username = user,item_tag = item_id)
    
    messages.success(request, 'Item added to cart successfully!')

    
    return redirect('home')


@login_required(login_url='login')
def cart_item_delete(request,item_id):
    user = request.user
    item_id = str(item_id)
    
    delete_item = CartItems.objects.filter(username = user,item_tag = item_id)
    delete_item.delete()
    return redirect('cart')

@login_required(login_url='login')
def cart_item_delete_all(request):
    user = request.user
    
    delete_all = CartItems.objects.filter(username = user)
    delete_all.delete()
    
    return redirect('cart')


# @login_required(login_url='login')
# def cart_buy_all(request):
#     user = User.objects.get(username = request.user.username)
#     carttag = CartItems.objects.filter(username = user).values_list('item_tag' ,flat=True)
    
#     items = ItemReg.objects.filter(id__in = carttag)
#     for item in items:
#         count += int(items.item_price)
#     print(count)
#     return render(request, 'cart_view.html', {'res': items})


# =======================================USER PROFILE===========================================

class ProfileView(LoginRequiredMixin,View):
    login_url = '/login/'
    
    def get(self,request,id=None,*args, **kwargs):
        user_id = request.user.id
        obj = get_object_or_404(Profile,id = user_id)
        
        return render(request,'profile.html',{'mesg':obj})
    
    
# =====================================USER HELP DESK =======================================

class HelpDesk(View):
    def get(self,request,*args, **kwargs):
        
        return render(request,'help.html',{'mesg':'hello user'})