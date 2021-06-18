from django.db import models

# Create your models here.
class Product(models.Model):
	title 		= models.CharField(	
							default="add title",	
							max_length=120) #max_length needed
	description = models.TextField(	
							default="add description",
							blank=True,
							null=True)
	price 		= models.DecimalField(	
							default=0.00,
							decimal_places=2,
							max_digits=7)
	summary 	= models.TextField(	
							default="This is pretty all cool")
	featured	= models.BooleanField() #null=True (datedase), default = True ()
