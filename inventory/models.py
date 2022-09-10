from django.db import models
class Device(models.Model):#name of the table
	type=models.CharField(max_length=10,blank=False)#name of the column
	price=models.IntegerField()
	choices =(
		('availlable','Item ready to be purchased'),
		('SOLD','Item sold'),
		('RESTOCKING','item restoking in few days'))
	status =models.CharField(max_length=10,choices=choices,default="SOLD")#availlable ,sold,restocking
	Issues=models.CharField(max_length=100,default="No Issues")
	class Meta:#this one it declare this class as the base class that will inherit the other classes
		abstract= True
	def __str__(self):
		return 'Type:{0}price:{1}'.format(self.type,self.price)
     
    
    
    	 
   	   
class Desktop(Device):#its inheriting everything from class device
	pass
    #we can add any other field thats not part of the device here
class Laptop(Device):#its inheriting everything from class device
	pass
    #we can add any other field thats not part of the device her

class Mobile(Device):#its inheriting everything from class device
	pass
    #we can add any other field thats not part of the device her




       	



# Create your models here.
