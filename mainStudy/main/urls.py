from django.urls import path, include
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:category_slug>', views.shop, name='shopCat'),
    path('shop/<int:page>/', views.shop, name='shopPage'),
    path('product/<slug:product_slug>/', views.product, name='product')
]