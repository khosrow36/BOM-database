from django.contrib import admin

from .models import Supplier, Part, Product, BOM

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'sell_price']
    list_display = ('name', 'sell_price')

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'supplier']
    list_display = ('name', 'price', 'supplier')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = ['name', 'info']
    list_display = ('name', 'info')

@admin.register(BOM)
class BOMAdmin(admin.ModelAdmin):
    fields = ['product', 'part', 'quantity']
    list_display = ('product', 'part', 'quantity')

admin.site.site_header = 'BOM Administracja'