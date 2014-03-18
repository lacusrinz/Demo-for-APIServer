from django.db import models
import json

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name

class Player(models.Model):
	name = models.CharField(max_length = 50)
	game = models.ForeignKey(Game)
	rating = models.IntegerField()

	def __unicode__(self):
		return self.name





		

