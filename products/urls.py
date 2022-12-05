from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
   path('', views.products, name="products"),
   path('add/', views.add_product, name="add"),
   path('add_product_action/', views.add_product_action, name="add_product_action"),
   path('search/', views.find_product, name="search"),
   path('delete/', views.delete_product, name="delete"),
   path('buy/',views.buy_product,name='buy_product'),
   path('index/',views.home,name='home'),
   path('<id>/',views.single_product,name='single_product'),
   path('orders/', views.orders, name="orders"),
    
]