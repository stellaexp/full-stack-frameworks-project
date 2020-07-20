from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name = 'view_bag'),
    path('add/<item_id>/', views.add_to_basket, name = 'add_to_basket'),
    path('edit/<item_id>/', views.edit_basket, name = 'edit_basket'),
    path('delete_item_from_basket/<item_id>/', views.delete_item_from_basket, name = 'delete_item_from_basket'),
]
