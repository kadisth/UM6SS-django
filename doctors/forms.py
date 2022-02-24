from django import forms

from doctors.models import Contact

# class ContactForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     subject = forms.CharField()
#     message = forms.CharField()
class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields= ("name","email","subject","message")