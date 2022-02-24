from django.contrib import admin 
from msilib.schema import DrLocator
from .models import Doctor
# Register your models here.
@admin.register(Doctor)
class Doctoradmin(admin.ModelAdmin):
   list_display = ()

#admin.site.register(Doctor)