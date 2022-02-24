from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
# Create your models here.


class Doctor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name="doctor",
        null=True
    )
    grade = models.CharField(
        _("fonction"),
        max_length=75,
        help_text=_("entez la fonction du docteur")
    )
    description = models.TextField(
        _("Description"),
        max_length=500,
        help_text=_("entez la description du docteur"),
        null=True
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)
    
    class Meta:
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")

    def __str__(self):
        return self.user.get_full_name()
        
class Contact(models.Model):
    name = models.CharField(
        
        _("name"),
        max_length=100,
        help_text=_("entez le nom")
    )
    email = models.EmailField(
        _("email"),
        max_length=100,
        help_text=_("entez l'email")
    )
    subject = models.CharField(
        _("subject"),
        max_length=100,
        help_text=_("entez le subject"),
        null=True
    )
    message = models.TextField(
        _("message"),
        max_length=500,
        help_text=_("entez le message"),
        null=True
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)
    
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name

