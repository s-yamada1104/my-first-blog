from django.db import models

# Create your models here.
from django.conf import settings
from django.db import migrations, models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime as dt

class  Member(models.Model):
  member_id = models.CharField("member_id", max_length = 100, unique = True, default = "")
  name = models.CharField("name", max_length = 100, blank = True)
  email = models.CharField("email", max_length = 1000, blank = True)
  points = models.IntegerField("points", blank = True, null = True)
  def __str__(self):
    return self.member_id


class Sell(models.Model):
  store_id = models.CharField("store_id", max_length = 100)
  payment_id = models.CharField("payment_id",max_length = 100)
  payment_method = models.CharField("payment_method",blank=True,max_length = 100)
  offering_method = models.CharField("offering_method",blank=True,max_length = 100)
  time = models.CharField("time",max_length = 100)
  product_id = models.CharField("product_id",blank=True,max_length = 100)
  product_name = models.CharField("product_name",blank=True,max_length = 100)
  price = models.IntegerField("price",blank=True,null = True)
  tax = models.CharField("tax",blank=True,max_length = 100)
  price_including_tax = models.IntegerField("price_including_tax")
  member_id = models.CharField("member_id", blank = True, max_length = 100, default = "")

  def __str__(self):
    return self.payment_id




 