from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Departments,Doctors,Booking



def index(request):
    dict_docs={
        "doctors":Doctors.objects.all()
    }
    return render(request,'index.html',dict_docs)

def booking(request):
  full_name = request.POST['full_name']
  email = request.POST['email']
  date = request.POST['date']
  p_number = request.POST['p_number']
  doc_name = request.POST['doc_name']
  member = Booking(full_name=full_name, email=email,date=date,p_number=p_number,doc_name=doc_name)
  member.save()
  return render(request,'confirmation.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        docs = Doctors.objects.filter(doc_name__contains = searched) |  Doctors.objects.filter(doc_spec__contains = searched) 
        return render(request,'searched.html',{'searched':searched,'docs':docs})
    else:
        return render(request,'searched.html',{})
