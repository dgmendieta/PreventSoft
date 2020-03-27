from django.db import models



#This class is for Tools, Herramientas y Equipos.
class Tool(models.Model):
	name = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='toolmedia/', null=True, blank=True)

	
	def __str__(self):
		return self.name


