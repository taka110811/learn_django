from django.contrib import admin
from .models import Product
from django.contrib.admin.sites import AlreadyRegistered

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)

try:
    admin.site.register(Product, ProductAdmin)
except AlreadyRegistered:
    pass