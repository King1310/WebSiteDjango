from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart_change/<int:product_id>/', views.cart_change, name='cart_change'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/update/<int:item_id>/', views.cart_update, name='cart_update'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('order_success/', views.order_success, name='order_success'),
]
