from django.urls import  path
from .views import *

urlpatterns = [
    path('cart_view/',cart_view,name='cart'),
    path('cart_add/<item_id>/',cart_add_item,name='cartadd'),
    path('cart_delete/<item_id>/',cart_item_delete,name='cartdelete'),
    path('cart_deleteall/',cart_item_delete_all,name='cartdeleteall'),
    path('profile/',ProfileView.as_view(),name='ProfileView'),
    path('help/',HelpDesk.as_view(),name='help'),
]
