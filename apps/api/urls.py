from django.urls import path
from .views import *
urlpatterns = [
    path('api-add/',add_list,name='add_list'),
    path('update_or_add_or_delete/',update_or_add_or_delete,name='update_or_add_or_delete'),
    path('ClsBase/',ClsBase.as_view(),name='ClsBase'),
    path('ClsBase/<int:id>/',ClsBase.as_view(),name='ClsBase1'),
    
]
