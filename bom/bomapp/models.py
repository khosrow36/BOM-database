from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=250)
    info = models.TextField()
    def __str__ (self):
        return self.name

class Part(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __str__ (self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__ (self):
        return self.name

class BOM(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    class Meta:
        verbose_name_plural = "BOM"