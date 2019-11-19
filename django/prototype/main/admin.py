from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

#To customize what is shown in the admin console
#Slim the fields down as follows
#Can also change the order with this method
#class TutorialAdmin(admin.ModelAdmin):
#	fields = ["tutorial_title"
#			  "tutorial_content"
#			  "tutorial_published"]

#Custom Sections 
class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
		("Content", {"fields": ["tutorial_content"]})
		]

#this will overwrite the orignal text field with the TinyMCE overlay
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
		}



admin.site.register(Tutorial, TutorialAdmin)


#Simple Version
# To display created model in Admin it needs to imported
#admin.site.register(Tutorial)