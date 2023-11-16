from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *

# Create your views here.

def home(request):
    d=student.objects.all()
    return render(request,'home.html',{'t':d})


from app1.form import*
def form1 (request):
    form=studentform()
    if(request.method=='POST'):
          form=studentform(request.POST)
          if(form.is_valid()):
                form.save()
                return home(request)
    return render(request,'form.html',{'form':form})
def form2 (request):
    form=studentform()
    if(request.method=='POST'):
          form=studentform(request.POST)
          if(form.is_valid()):
                form.save()
                return home(request)
    return render(request,'form2.html',)

