from django.db import models

from django.contrib.auth.models import User
from tool.models import Tool
from EPP.models import EPP
from hazard.models import Hazard
from precaution.models import Precaution

#For future dynamic and personalizable Status
class APRStatus(models.Model):
	pass

#This is for auto set the number of a new document
#and don´t mess with the id of documents
def set_documentnumber():
	value = APR.objects.all().order_by('documentnumber').last()
	if value is None:
		new_documentnumber = 1
	else:	
		new_documentnumber = value.documentnumber + 1

	return new_documentnumber


#This class is the document, the user is auto set
#when a new document is created, takes the logged user
#the date and set de document number
class APR(models.Model):

	title = models.CharField(max_length=50, null=False, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	documentnumber = models.IntegerField(null=False, blank=False, unique=False, default=set_documentnumber)
	comments = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
	#The status is hardcoded now, but will change in future.
	APR_STATUS = (
        ('Iniciado', 'Iniciado'),
        ('Completado', 'Completado'),
        ('Cancelado', 'Cancelado'),
    )

	status = models.CharField(max_length=50, choices=APR_STATUS, null=False, blank=False)

	#Shows the title in admin of Django
	def __str__(self):
		return self.title





#This class is for documents lines. We have to improve it
#because if you edit or delete, for example, a tool, 
#the document line will going to change.
class APRLine(models.Model):

	activities = models.TextField(blank=False, null=False)
	apr = models.ForeignKey(APR, on_delete=models.CASCADE)
	tools = models.ManyToManyField(Tool, blank=True)
	epps = models.ManyToManyField(EPP, blank=True)
	hazards = models.ManyToManyField(Hazard, blank=True)
	precautions = models.ManyToManyField(Precaution, blank=True)

	#Shows the title in admin of Django
	def __str__(self):
		return self.apr.title
