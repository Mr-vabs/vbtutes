from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
  #return HttpResponse("testing homepage");
  return render(request, 'index.htm')
def about(request):
  #return HttpResponse("testing about page");
  return render(request, 'about.htm')
def contact(request):
  if request.method == 'POST' :
    name = request.POST.get('name')
    email = request.POST.get('email')
    number = request.POST.get('number')
    description = request.POST.get('description')
    contact = Contact(name=name, email=email, number=number, description=description, date=datetime.today())
    contact.save()
    messages.success(request, 'Your message has been sent!')
  #return HttpResponse("testing contact page");
  return render(request, 'contact.htm')
def services(request):
  #return HttpResponse("testing services page");
  return render(request, 'services.htm')