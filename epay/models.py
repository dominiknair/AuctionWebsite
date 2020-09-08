from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal

# Create your models here.
class Item(models.Model):
    itemTitle = models.CharField(max_length=40)
    # time =  models.TimeField(default)
    itemDescription = models.TextField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0.00'))
    endTime = models.DateField(max_length=8)
    itemPicture = models.ImageField(default='default.jpg',upload_to ='item_pics')
    date_listed = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    Isopen = models.BooleanField(null = True,default=True)
    winner = models.ForeignKey(User,on_delete=models.CASCADE,related_name = '+',null=True,blank = True)
    currentBid = models.DecimalField(blank = True,default=Decimal('0.00'),decimal_places=2, max_digits=12)
    biddings = models.CharField(max_length=100000,blank = True)

    def __str__(self):
       return str(self.itemTitle)
       return self.itemDescription
       return self.price
       return self.endTime
       return self.itemPicture
       return self.seller

    def get_absolute_url(self):
        return reverse('item-detail',kwargs = {'pk':self.pk})

class Bid(models.Model):
    Timestamp =  models.TimeField(auto_now_add=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE,related_name = '+',null=True,blank = True)
    item =  models.ForeignKey(Item,on_delete=models.CASCADE,related_name = '+',null=True,blank = True)
    AmountBid = models.DecimalField(blank = True,default=Decimal('0.00'),decimal_places=2, max_digits=12)

    def __str__(self):
       return str(self.bidder)
       return self.item
       return self.AmountBid
