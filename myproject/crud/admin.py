from django.contrib import admin
from .models import Product, Category
from django.contrib.admin.sites import AlreadyRegistered

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

try:
    admin.site.register(Product, ProductAdmin)
    admin.site.register(Category, CategoryAdmin)
except AlreadyRegistered:
    pass