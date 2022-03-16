from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Purchase(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default = 'c',
        max_length=1,
        choices=(('A','Approved'),
        ('C','Created'),
        ('D','Disapproved'),
        ('P','Pending'),
        ('S','Sent'),
        ('F','Finished'),
        )
    )

    def __str__(self):
        return f"Purchase nº: {self.pk}"

class PurchaseItems(models.Model):

    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    price = models.FloatField(default=0)
    image = models.CharField(max_length=2000)

    def __str__(self):
        return f"Item of {self.pedido}"
    
    class Meta():
        verbose_name = "Item of purchase"
        verbose_name_plural = "Items of purchase"
    