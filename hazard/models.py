from django.db import models

from tool.models import Tool

#This class is for Hazards, Peligros y Riesgos
#Is related to the Tool class, because
#in the future it will be possible to learn which 
#relationships are more used and how they are used
class Hazard(models.Model):

	name = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	tools = models.ManyToManyField(Tool, blank=True)
	
	#Shows the title in admin of Django
	def __str__(self):
		return self.name
