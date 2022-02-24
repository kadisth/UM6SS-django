from msilib.schema import DrLocator
from django.contrib import admin
from .models import Doctor,Contact 
# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("user","grade","description", "created_at", "modified_at")
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","email","subject","message" ,"created_at", "modified_at")
    

# admin.site.register(Doctor)

