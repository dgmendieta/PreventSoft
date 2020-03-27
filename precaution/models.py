from django.db import models

from hazard.models import Hazard

#This class is for Precaution, Medidas Preventivas
#Is related to the Hazard class, because
#in the future it will be possible to learn which 
#relationships are more used and how they are used
class Precaution(models.Model):

	name = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	precautions = models.ManyToManyField(Hazard, blank=True)
	
	#Shows the title in admin of Django
	def __str__(self):
		return self.name
