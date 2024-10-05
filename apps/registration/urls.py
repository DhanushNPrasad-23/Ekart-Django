from django.urls import path


from .views import *

urlpatterns = [
    path('Home/',home,name="home"),
    path('',user_login,name='login'),
    path('Home/<str:item_type>/', home, name="home_with_type"),
    path('Logout/',logout_user,name='logout'),
    path('Register_user/',user_reg,name='register_user'),
    path('user-view-admin/',TotalUser.as_view(),name='TotalUser'),
    path('user-view-admin/<int:id>',TotalUser.as_view(),name='TotalUserdelete'),
    path('userupadate/<int:id>/',usermodi,name='usermodi'),
    path('Item_reg/',item_reg,name='item_reg'),
    path('update_delete_item_page/',update_delete_item_page,name='update_delete_item_page'),
    path('update_delete_item_delete/<id>/',update_delete_item_delete,name='update_delete_item_delete'),
    path('update_delete_item_update/<id>/',update_delete_item_update,name='update_delete_item_update'),
]
