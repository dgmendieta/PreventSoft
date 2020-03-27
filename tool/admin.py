from django.contrib import admin

from .models import Tool

class ToolAdmin(admin.ModelAdmin):
	fields = ('name', 'image',)
	list_display = ('__str__', 'created_at', 'image',)

admin.site.register(Tool, ToolAdmin)


