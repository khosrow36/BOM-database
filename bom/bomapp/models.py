from django.db import models

class Suppliers(models.Model):
    name = models.CharField(max_length=250)
    info = models.TextField()

class Parts(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)


class Products(models.Model):
    name = models.CharField(max_length=250)
    parts = models.ForeignKey(Parts, on_delete=models.CASCADE)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)