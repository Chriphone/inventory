from django.shortcuts import render,redirect,get_object_or_404
from.models import *
from .forms import*
def index(request):
	return render(request, 'index.html')

def display_laptops(request):
	items= Laptop.objects.all()
	context = {
	'items':items,
	'header':'Laptops'

	}
	return render(request, 'index.html',context)
def display_desktop(request):
	items= Desktop.objects.all()
	context = {
	'items':items,
	'header':'Desktops'

	}
	return render(request, 'index.html',context)
def display_mobile(request):
	items= Mobile.objects.all()
	context = {
	'items':items,
	'header':'Mobiles'

	}
	return render(request, 'index.html',context)
'''
def add_laptop(request):#this  is a function to stat adding item  from the form
	if request.method == "POST":
		#if you  have entered the information and  you press the url  the form is posting the data and  the POSTrequest will be executed
		form= LaptopForm(request.POST)# this  is how we are validating the form
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form=LaptopForm()#if theirs no information currently of the form and the url has been accessed then it will return an empty form and thhis part will be executed and it will be a get request
		return render(request,'add_new.html',{'form':form})
'''
	#insteady of writing more cords on how to add   other devices we can do the follwing
def add_device(request,cls):#change this to be add device and its going to take class as a parameter
	if request.method == "POST":
		#if you  have entered the information and  you press the url  the form is posting the data and  the POSTrequest will be executed
		form= cls(request.POST)# instead of laptopform we put cls this  is how we are validating the form
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form=cls()#if theirs no information currently of the form and the url has been accessed then it will return an empty form and thhis part will be executed and it will be a get request
		return render(request,'add_new.html',{'form':form})
#im going to take advantage that everythin is an object in python
def add_laptop(request):
	return add_device(request,LaptopForm)

def add_desktop(request):
	return add_device(request,DesktopForm)
def add_mobile(request):
	return add_device(request,MobileForm)
'''
we can  coppy thhis and replace it with other device
def edit_laptop(request,pk):
	item=get_object_or_404(Laptop,pk=pk)#its trying to get a specific object  from the laptop that has  laptop its basically like select items  with  speccific field
	if request.method =="POST":
		form=LaptopForm(request.POST,instance=item)#The form is going to display/populalate the item
		if form.is_valid():
			form.save()
			return redirect('index')


	else:
		form=LaptopForm(instance=item)#instance means display the information of an item which we had included before
		return render(request,'edit_item.html',{'form':form})
'''
#we can also geralize this a device as follows
def edit_laptop(request,venue_id):#its going to take other  parameter like
	item=Laptop.objects.get(pk=venue_id)#we subtitute laptop with model
	if request.method =="POST":
		form=LaptopForm(request.POST,instance=item)#substitute LaptopForm with cls
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form= LaptopForm(instance=item)#substitute LaptopForm with cls
		return render(request,'edit_item.html',{'item':item,'form':form})
def edit_desktop(request,venue_id):#its going to take other  parameter like
	item=Desktop.objects.get(pk=venue_id)#we subtitute laptop with model
	if request.method =="POST":
		form=DesktopForm(request.POST,instance=item)#substitute LaptopForm with cls
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form= DesktopForm(instance=item)#substitute LaptopForm with cls
		return render(request,'edit_item.html',{'item':item,'form':form})
def edit_mobile(request,venue_id):#its going to take other  parameter like
	item=Mobile.objects.get(pk=venue_id)#we subtitute laptop with model
	if request.method =="POST":
		form=MobileForm(request.POST,instance=item)#substitute LaptopForm with cls
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form= MobileForm(instance=item)#substitute LaptopForm with cls
		return render(request,'edit_item.html',{'item':item,'form':form})
def delete_laptop(request,venue_id):
	Laptop.objects.filter(pk=venue_id).delete()
	items=Laptop.objects.all()
	context={
	"items":items,
	'header':'Laptops'
	}
	return render(request,'index.html',context)

def delete_desktop(request,venue_id):
	Desktop.objects.filter(pk=venue_id).delete()
	items=Desktop.objects.all()
	context={
	"items":items,
	'header':'Desktops'
	}
	return render(request,'index.html',context)

def delete_mobile(request,venue_id):
	Mobile.objects.filter(pk=venue_id).delete()
	items=Mobile.objects.all()
	context={
	"items":items,
	'header':'Mobiles'
	}
	return render(request,'index.html',context)
