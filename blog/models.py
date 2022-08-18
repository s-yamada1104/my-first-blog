from django.conf import settings
from django.db import migrations, models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime as dt

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class User(models.Model):
#   user_id = models.CharField("user_id", unique = True)
#   name = models.CharField("user_name", max_length = 100,blank=True)
#   email = models.EmailField(("email"),blank=True)
#   points = models.IntegerField("points", default = 0,blank=True)
#   def __str__(self):
#     return self.user_id

class Sales(models.Model):
  store_id = models.CharField("store_id", max_length = 100)
  payment_id = models.CharField("payment_id", unique = True,max_length = 100)
  payment_method = models.CharField("payment_method",blank=True,max_length = 100)
  offering_method = models.CharField("offering_method",blank=True,max_length = 100)
  time = models.DateTimeField("time")
  product_id = models.CharField("product_id",blank=True,max_length = 100)
  product_name = models.CharField("product_name",blank=True,max_length = 100)
  price = models.IntegerField("price",blank=True)
  tax = models.CharField("tax",blank=True,max_length = 100)
  price_including_tax = models.IntegerField("price_including_tax")
  user_id = models.CharField("user_id", blank = True,max_length = 100)
  def __str__(self):
    self.payment_id


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
  member_id = models.ForeignKey(Member,verbose_name = "member_id", blank = True, null = True, max_length = 100, on_delete = models.PROTECT, to_field = "member_id")

  def __str__(self):
    return self.payment_id




 