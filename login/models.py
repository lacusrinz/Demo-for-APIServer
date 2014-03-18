from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length = 50)
	password = models.CharField(max_length = 256)
	email = models.EmailField(blank = True)
	
	def __unicode__(self):
		return self.name
