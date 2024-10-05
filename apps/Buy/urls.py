from django.urls import path
from .views import *

urlpatterns = [
    path('buy/<id>/',buy_page,name='buy_page'),
    path('item_det/<id>/',item_view,name='item_view'),
    path('your_orders/',your_orders,name='your_orders'),
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]
