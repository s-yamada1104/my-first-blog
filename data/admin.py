from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Sell, Member


admin.site.register(Sell)
admin.site.register(Member)