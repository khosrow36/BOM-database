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
    parts = models.ManyToManyField(Part)
    def __str__ (self):
        return self.name

    def parts_cost(self):
        cost = 0
        for part in self.parts.all():
            cost = cost + part.price
        return cost

    def product_margin(self):
        return self.sell_price - self.parts_cost()