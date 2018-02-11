from django.contrib import admin
from recuperer.models import coordonnee

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ['longitude', 'latitude', 'vitesse','heading', 'date',]
	list_filter = ['heading',]
	date_hierarchy = 'date'
	ordering = ['date',]
admin.site.register(coordonnee,PostAdmin)

