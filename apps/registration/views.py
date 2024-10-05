from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login , logout as auth_logout,authenticate
from .forms import *
from django.db.models import F, OuterRef, Subquery


# Create your views here.
# =============================================LOGIN=================================


def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginUserForm()

    return render(request, 'login.html', {'form': form})

# ===============================================HOME PAGE===================================================


def home(request,item_type=None):
    if item_type:
        obj = ItemReg.objects.filter(item_type = item_type)
        items = ItemReg.objects.filter(item_type = item_type)
    else:
        obj = ItemReg.objects.all()
        subquery = ItemReg.objects.filter(item_type=OuterRef('item_type')).values('id')[:1]

        items = ItemReg.objects.annotate(
            first_item_id=Subquery(subquery)
        ).filter(id=F('first_item_id'))
    
    
    return render(request,'home.html',{'mesg':obj,'items':items})

# =================================================LOGOUT=====================================================

@login_required(redirect_field_name='login')
def logout_user(request):
    auth_logout(request)
    return redirect('login')
    
# ==========================================REGISTER USER=======================================================

def user_reg(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            p_number = form.cleaned_data['p_number']

            user = User.objects.create(username=username)
            user.set_password(password)  
            user.save()

            Profile.objects.create(user=user, p_number=p_number)

            return redirect('home')  
        else:
            form.add_error(None, 'Invalid credentials')
    else:
        form = UserRegister()

    return render(request, 'register_user.html', {'form': form})

# =======================================ITEM_REGISTER=======================================================


@login_required(redirect_field_name='login')
def item_reg(request):
    if request.method == 'POST':
        form = ItemRegister(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form.add_error('','invalid item given')
    else:
        form  = ItemRegister()
        
    return render(request,'item_register.html',{'form':form})


# =================================DELETE_ITEM OR UPDATE_ITEM ================================================

@login_required(redirect_field_name='login')
def update_delete_item_page(request):
    obj  = ItemReg.objects.all()
    
    return render(request,'Updatedelete.html',{'res':obj})


# ==================================DELETE ITEM===============================================================

def update_delete_item_delete(request,id):
    obj1 = ItemReg.objects.filter(id = id)
    obj1.delete()
    obj  = ItemReg.objects.all()
    
    return render(request,'Updatedelete.html',{'res':obj})

# =============================UPDATE ITEM ====================================================================


def update_delete_item_update(request,id):
    item  = get_object_or_404(ItemReg,id = id)        
    
    if request.method == 'POST':
         form = ItemRegister(request.POST, request.FILES, instance=item)
         if form.is_valid():
            form.save()   
            return redirect('update_delete_item_page') 
    
    else:
        form = ItemRegister(instance=item)
        
    return render(request,'Update_item.html',{'form':form})
    
# ==================================TOTAL USERS IN SUPERUSER ==============================================

class TotalUser(View):
    
    def get(self,request,*args, **kwargs):
        data = Profile.objects.all()
        return render(request,'userview.html',context={'profiles':data})
    
    def post(self,request,id,*args, **kwargs):
        
        data1 = get_object_or_404(User,id=id)
        if data1:
            data1.delete()
            data = Profile.objects.all()
            
            return redirect('TotalUser')

# ===============================================USER MODIFICATION =======================================
    
def usermodi(request,id):
    profile = get_object_or_404(Profile,id=id)
    
    form = None
    
    if request.method == 'PATCH':
        form = UserRegister(request.PATCH,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('TotalUser')
        else: 
            form = form.add_error('','invalid data given')
    else:
        form = UserRegister(instance=profile.user)
        
    return render(request,'userupdate.html',context={'form':form})

