from django.db import models


# Create your models here.

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Category(models.Model):
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title


class Property(models.Model):
	title = models.CharField(max_length = 210,default = 'None')

	STATUS_CHOICES = (
	('RENT','Rent'),
	('SALE','Sale'),
		)

	status = models.CharField(max_length = 210,choices = STATUS_CHOICES,default = 'Rent')

	price = models.IntegerField()
	
	area = models.CharField(max_length = 210,default = 'None')

	ROOM_CHOICES = (
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('MORE','More'),
		)

	rooms = models.CharField(max_length = 210,choices = ROOM_CHOICES,default = '1')
	BATHROOM_CHOICES = (
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	)
	bathroom = models.CharField(max_length = 210,choices = BATHROOM_CHOICES,default = '2')
	address = models.CharField(max_length = 210,default = 'None')

	STATE_CHOICES = (
		('CA','California'),
		('NY','New york'),
		('C','Chicago'),

		)

	state = models.CharField(max_length = 210,default = 'None',choices = STATE_CHOICES)
	code = models.CharField(max_length = 210,default = 'None')
	images = models.ImageField(upload_to = 'images',default = 'images/20190327_154648_0001.png')
	info = models.TextField(max_length = 1000,default = 'None')
	parking = models.BooleanField(default = False,verbose_name = 'Parking')
	air = models.BooleanField(default = False)
	swimming = models.BooleanField(default = False)
	laundry = models.BooleanField(default = False)
	dealer_name = models.CharField(max_length = 210,default = 'None')
	dealer_email = models.EmailField(max_length = 210,default = 'abc@gmail.com')
	dealer_number = models.CharField(max_length = 210,default = 'Not mentioned')
	user = models.ForeignKey(User,related_name = 'user',default = True)
	timpestamp = models.DateTimeField(auto_now_add = True)
	category = models.ManyToManyField(Category,related_name = 'categories',default = None)


	def get_absolute_url(self,*args,**kwargs):
		return reverse('profile_details:property')

	def __str__(self):
		return self.title



