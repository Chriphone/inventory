from django import forms
from .models import *

#to define the form it must exactly corespond to the model that we defined earlier thats
class LaptopForm(forms.ModelForm):#we are importing laptop form from the model form
	class Meta:
		model=Laptop
		fields =('type','price','status','Issues')


class DesktopForm(forms.ModelForm):#we are importing laptop form from the model form
	class Meta:
		model=Desktop
		fields =('type','price','status','Issues')
	

class MobileForm(forms.ModelForm):#we are importing laptop form from the model form
	class Meta:
		model=Mobile
		fields =('type','price','status','Issues')


	
