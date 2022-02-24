from django.http import HttpResponse
from django.shortcuts import render
from .models import Doctor
from .forms import ContactForm

def index(request):
    context = {
        "doctors": Doctor.objects.all(),
        "forms": ContactForm()
    }
    if request.method == "POST":
        f=ContactForm(request.POST)
        print(request.POST)
        if f.is_valid():
            contact=f.save(commit=False)
            contact.save()

    
    return render(request,'index.html',context)
def home(request):
    context = {
        "doctors": Doctor.objects.all()
    }
    return render(request,'home.html',context)