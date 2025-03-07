from django.shortcuts import render,redirect,get_object_or_404

from app.forms import PersonForm
from app.models import Person
from django.contrib import messages



# Create your views here.
def index(request):
    if request.method == "POST":
        form = PersonForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PersonForm()
    return render(request, 'index.html',{'form':form})

def person_list(request):
    data=Person.objects.all()
    return render(request, 'list.html',{'data':data})

def edit_person(request,id):
    person = get_object_or_404(Person,id=id)
    if request.method == "POST":
        form = PersonForm(request.POST,request.FILES,instance=person)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = PersonForm(instance=person)
    return render(request, 'edit_list.html',{'form':form,'person':person})
def delete_person(request,id):
    student = get_object_or_404(Person,id=id)
    try:
        student.delete()
    except Exception as e:
        messages.error(request,"person not deleted")
    return redirect("person_list")

