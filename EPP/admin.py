from django.contrib import admin

from .models import EPP

#Shows the fields in admin of Django
class EPPAdmin(admin.ModelAdmin):
	fields = ('name', 'image',)
	list_display = ('__str__', 'created_at', 'image',)

admin.site.register(EPP)

