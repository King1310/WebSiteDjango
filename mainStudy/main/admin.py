from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.models import Category, Product

#admin.site.register(Category)
#admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
