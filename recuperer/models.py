from django.db import models


# Create your models here.

class coordonnee(models.Model):
	  latitude = models.FloatField(default = 0.0)
	  longitude = models.FloatField(default = 0.0)
	  vitesse = models.FloatField(default = 0.0)
	  date = models.DateTimeField(auto_now = False,auto_now_add = False)
	  heading = models.IntegerField(default = 0)

	  class Meta:
	  	def __str__(self):
	  		return self.latitude, self.longitude

