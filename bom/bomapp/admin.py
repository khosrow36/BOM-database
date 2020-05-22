from django.contrib import admin

from .models import Supplier, Part, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'parts', 'sell_price']

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'supplier']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = ['name', 'info']


admin.site.site_header = 'BOM Database Admin Panel'