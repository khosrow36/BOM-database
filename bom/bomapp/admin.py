from django.contrib import admin

from .models import Supplier, Part, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'sell_price', 'parts']
    list_display = ('name', 'sell_price')

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'supplier']
    list_display = ('name', 'price', 'supplier')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = ['name', 'info']
    list_display = ('name', 'info')

admin.site.site_header = 'BOM Administracja'