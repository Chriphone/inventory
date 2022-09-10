from django.contrib import admin
from .models import *
@admin.register(Desktop,Laptop,Mobile)#class decorator
class ViewAdmin(admin.ModelAdmin):#we are calling a class view admin its inheriting admin.modeladmin
   pass

# Register your models here.
