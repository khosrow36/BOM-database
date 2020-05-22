from django.contrib import admin

from .models import Supplier, Part, Product, BOM

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'sell_price']

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'supplier']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = ['name', 'info']

@admin.register(BOM)
class BOMAdmin(admin.ModelAdmin):
    fields = ['product', 'part', 'quantity']

admin.site.site_header = 'BOM Administracja'