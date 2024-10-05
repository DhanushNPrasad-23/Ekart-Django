
# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from eKart import settings
from apps.registration.models import ItemReg,Profile
from .models import Buy,Order
from .forms import BuyForm
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.orders.models import OrderHistory,History
from django.core.mail import send_mail


# ===========================================SEND MAIL INCLUDES THE SETTING ====================================
def send_order_confirmation_email(user_email):
    subject = 'Order Confirmation'
    message = 'Thank you for your order! Your order has been received and is being processed.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]  # List of recipients

    send_mail(subject, message, email_from, recipient_list)
    
    
    
# ===================================================PAGE OF SENDING THE MAIL=====================================
    
def buy_page(request,id):
    obj  = ItemReg.objects.get(id=id)
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_order_confirmation_email(email) 
            user = request.user
            use = get_object_or_404(User,username = user)
            it = ItemReg.objects.get(item_name = obj.item_name)
            History.objects.create(item = it,user = use)
            
            return redirect('home')
        else:
            form.add_error('','invalid request')
    else:
        form = BuyForm()
    
    return render(request,'buy_page.html',{'form':form,
                                           'item':obj})
    
# ==================================================ITEM VIEW=====================================================


def item_view(request,id):
    try:
        obj = ItemReg.objects.get(id=id)
    except:
        return render(request,'item_view.html',{'item':"obj",'mesg':'Item as been removed'})
    return render(request,'item_view.html',{'item':obj,'mesg':''})


# =====================================================YOUR ORDERS ============================================


def your_orders(request):
    user = User.objects.get(username = request.user)
    res = History.objects.filter(user = user)
    for order in res:
        print(order.order_date)
    
    
    return render(request,'yourorders.html',{'orders':res})

#======================================================Order History==========================================================


class OrderHistoryView(View):
    def get(self,request,*args, **kwargs):
        user = request.user
        obj = History.objects.filter(user = user)
        return render(request,'yourorders.html',{'obj':obj})
    





# ============================================================================================================






























@api_view(['GET'])
def first(request):
    return Response({
        'status' : 400,
        'read' : ' this is the first api written',
    })

@api_view(['GET','PUT','POST'])
def second(request):
    if request.method == 'POST':
        return Response({
            'status': 400,
            'read' : 'invalid method attempted',
        })
    elif request.method == 'GET':
        return Response({
            'status': 200,
            'read' : 'this is get method',
        })