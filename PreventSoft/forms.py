from django import forms

from django.contrib.auth.models import User
from APR.models import APR, APRLine
from EPP.models import EPP
from hazard.models import Hazard
from precaution.models import Precaution
from tool.models import Tool



#### Forms from User class ####
#Form to create a new user. Only admin
#users can use it	
class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','email','is_superuser','password')
		labels = {
			'username': 'Correo Electrónico',
			'email': 'Repetir Correo',
			'is_superuser': 'Usuario Administrador?',
			'password': 'Clave'
		}
		widgets = {
			'username': forms.EmailInput(attrs={'class':'form-control', 
												'placeholder': 'Ingrese el correo'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 
										'onblur' : "checkEmail(this)", 
										'placeholder': 'Confirme el correo'}),
			'is_superuser': forms.CheckboxInput(attrs={'class':'form-check-input'}),
			'password' : forms.PasswordInput(attrs={'class':'form-control', 
													'placeholder': 'Ingrese la clave'}),
		}
		help_texts = {
			'username' : "*Ingrese su correo electrónico",
			'is_superuser' : "*Marque la casilla si es usuario administrador",
		}
	
	#This method check if exists the username, because
	#the username must be unique
	def clean_username(self):
		username = self.cleaned_data.get('username')

		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('El nombre de usuario ya fué usado')

		return username	

	#This method check if exists the email, because
	#the email must be unique	
	def clean_email(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo ya fué usado')

		return email

#Form to edit users. Only admin
#users can use it
class EditUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','email','is_superuser','password')
		labels = {
			'username': 'Correo Electrónico',
			'email': 'Repetir Correo',
			'is_superuser': 'Usuario Administrador?',
			'password': 'Clave'
		}
		widgets = {
			'username': forms.EmailInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 
											'onblur' : "checkEmail(this)"}),
			'is_superuser': forms.CheckboxInput(attrs={'class':'form-check-input'}),
			'password' : forms.PasswordInput(attrs={'class':'form-control',}),
		}
		help_texts = {
			'username' : "*Ingrese su correo electrónico",
			'is_superuser' : "*Marque la casilla si es usuario administrador",
		}

#### End of Forms from User class ####

#### Forms from APR and APRLine class ####
  #These two forms will render at the same template AprForm and AprLineForm
#This form give the header of a document. The field documentnumber isn't called
#because if you have many documents in process when you want to save it 
#would generate an error
class AprForm(forms.ModelForm):
	class Meta:
		model = APR
		fields = ('title','comments','status')
		labels = {
			'title': 'Nombre del Documento',
			'comments': 'Comentarios',
			'status': 'Estado'
		}
		widgets = {
			'title': forms.Textarea(attrs={'class':'form-control','cols':'20','rows':'3'}),
			'comments': forms.Textarea(attrs={'class':'form-control','cols':'20','rows':'3'}),
		}
		help_texts = {
			'title' : '*Ingrese el título del documento',
			'comments' : "*Ingrese los comentarios correspondientes al documento",
			'status' : "*Defina el estado del documento",
		}


class AprEditForm(forms.ModelForm):
	class Meta:
		model = APR
		fields = ('title','documentnumber','comments','user','status')
		labels = {
			'title': 'Nombre del Documento',
			'comments': 'Comentarios',
			'status': 'Estado'
		}
		widgets = {
			'title': forms.Textarea(attrs={'class':'form-control','cols':'20','rows':'3'}),
			'documentnumber': forms.TextInput(attrs={'type':'hidden'}),
			'user': forms.TextInput(attrs={'type':'hidden'}),
			'comments': forms.Textarea(attrs={'class':'form-control','cols':'20','rows':'3'}),
		}
		help_texts = {
			'title' : '*Ingrese el título del documento',
			'comments' : "*Ingrese los comentarios correspondientes al documento",
			'status' : "*Defina el estado del documento",
		}



 # This form becomes in a inlineformset in views.py
 # to can save many lines for each document


class AprLineForm(forms.ModelForm):
	class Meta:
		model = APRLine
		fields = ('activities','apr','tools','epps','hazards','precautions')
		labels = {
			'activities': 'Actividades a Realizar',
			'tools': 'Herramientas a Utilizar',
			'epps': 'Eq Protección Personal',
			'hazards': 'Peligros y Riesgos',
			'precautions': 'Medidas Preventivas',
		}
		widgets = {
			'activities': forms.Textarea(attrs={'class':'form-control','cols':'20','rows':'3'}),
			'tools': forms.SelectMultiple(attrs={'class':'form-control'}),
			'epps': forms.SelectMultiple(attrs={'class':'form-control','cols':'30','rows':'5'}),
			'hazards': forms.SelectMultiple(attrs={'class':'form-control','cols':'30','rows':'5'}),
			'precautions': forms.SelectMultiple(attrs={'class':'form-control','cols':'30','rows':'5'}),
		}
		help_texts = {
			'activities' : '*Describa las actividades a realizar',
			'tools' : "*Mantenga presionada Control (Command en una Mac) para seleccionar más de uno",
			'epps' : "*Mantenga presionada Control (Command en una Mac) para seleccionar más de uno",
			'hazards' : "*Mantenga presionada Control (Command en una Mac) para seleccionar más de uno",
			'precautions' : "*Mantenga presionada Control (Command en una Mac) para seleccionar más de uno",
		}

class AprLineEditForm(forms.ModelForm):
	class Meta:
		model = APRLine
		fields = ('activities','apr','tools','epps','hazards','precautions')
		labels = {
			'activities': 'Actividades a Realizar',
			'tools': 'Herramientas a Utilizar',
			'epps': 'Eq Protección Personal',
			'hazards': 'Peligros y Riesgos',
			'precautions': 'Medidas Preventivas',
		}
		widgets = {
			'activities': forms.Textarea(attrs={'class':'form-control','cols':'20','rows':'3'}),
			'tools': forms.SelectMultiple(attrs={'class':'form-control'}),
			'epps': forms.SelectMultiple(attrs={'class':'form-control','cols':'30','rows':'5'}),
			'hazards': forms.SelectMultiple(attrs={'class':'form-control','cols':'30','rows':'5'}),
			'precautions': forms.SelectMultiple(attrs={'class':'form-control','cols':'30','rows':'5'}),
		}
		help_texts = {
			'activities' : '*Describa las actividades a realizar',
			'tools' : "*Mantenga presionada Control (Command en una Mac) para seleccionar más de uno",
			'epps' : "*Mantenga presionada Control (Command en una Mac) para seleccionar más de uno",
			'hazards' : "*Mantenga presionada Control (Command en una Mac) para seleccionar más de uno",
			'precautions' : "*Mantenga presionada Control (Command en una Mac) para seleccionar más de uno",
		}



#### End of Forms from APR and APRLine class ####

#### Forms from EPP class ####
#Form to create a new EPP. Only admin
#users can use it
class EppForm(forms.ModelForm):
	class Meta:
		model = EPP
		fields = ('name','image',)
		labels = {
			'name': 'Nombre del E.P.P.',
			'image': 'Puede subir una imagen',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 
											'placeholder': 'Ingrese el nombre'}),
			'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
		}
		help_texts = {
			
		}
	
	#This method check if exists the name, because
	#the name must be unique
	def clean_name(self):
		name = self.cleaned_data.get('name')

		if EPP.objects.filter(name=name).exists():
			raise forms.ValidationError('El nombre de E.P.P. ya fué usado')

		return name	
		

#Form to edit a EPP. Only admin
#users can use it
#We don´t know why, but if we use the same form
#who create epp, the image don´t upload and  
#data isn´t saved ???
class EppEditForm(forms.ModelForm):
	class Meta:
		model = EPP
		fields = ('name','image',)
		labels = {
			'name': 'Nombre del E.P.P.',
			'image': 'Cambiar o subir una imagen',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 
											'placeholder': 'Ingrese el nombre'}),
			'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
		}
		help_texts = {
			
		}	

#### End of Forms from EPP class #### 

#### Forms from Hazard class ####

#Form to create and edit a new Hazard. Only admin
#users can use it
class HazardForm(forms.ModelForm):
	class Meta:
		model = Hazard
		fields = ('name',)
		labels = {
			'name': 'Nombre del Peligro o Riesgo',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 
											'placeholder': 'Ingrese el nombre'}),
		}
		help_texts = {
			
		}
	
	#This method check if exists the name, because
	#the name must be unique
	def clean_name(self):
		name = self.cleaned_data.get('name')

		if Hazard.objects.filter(name=name).exists():
			raise forms.ValidationError('El nombre del Peligro ya fué usado')

		return name	 

#### End of Forms from Hazard class ####

#### Forms from Precaution class ####

#Form to create and edit a new Precaution. Only admin
#users can use it
class PrecautionForm(forms.ModelForm):
	class Meta:
		model = Precaution
		fields = ('name',)
		labels = {
			'name': 'Nombre de la Medida Preventiva o Precaución',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 
											'placeholder': 'Ingrese el nombre'}),
		}
		help_texts = {
			
		}
	
	#This method check if exists the name, because
	#the name must be unique
	def clean_name(self):
		name = self.cleaned_data.get('name')

		if Precaution.objects.filter(name=name).exists():
			raise forms.ValidationError('El nombre de Precaución ya fué usado')

		return name	  

#### End of Forms from Precaution class ####

#### Forms from Tool class ####
#Form to create a new Tool. Only admin
#users can use it
class ToolForm(forms.ModelForm):
	class Meta:
		model = Tool
		fields = ('name', 'image',)
		labels = {
			'name': 'Nombre de la Herramienta',
			'image': 'Puede subir una imagen',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 
											'placeholder': 'Ingrese el nombre'}),
			'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
		}
		help_texts = {
			
		}
	
	#This method check if exists the name, because
	#the name must be unique
	def clean_name(self):
		name = self.cleaned_data.get('name')

		if Tool.objects.filter(name=name).exists():
			raise forms.ValidationError('El nombre de la Herramienta ya fué usado')

		return name	  

#Form to edit a Tool. Only admin
#users can use it
#We don´t know why, but if we use the same form
#who create tool, the image don´t upload and  
#data isn´t saved ???
class ToolEditForm(forms.ModelForm):
	class Meta:
		model = Tool
		fields = ('name', 'image',)
		labels = {
			'name': 'Nombre de la Herramienta',
			'image': 'Puede subir una imagen',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 
											'placeholder': 'Ingrese el nombre'}),
			'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
		}
		help_texts = {
			
		}
#### End of Forms from Tool class ####