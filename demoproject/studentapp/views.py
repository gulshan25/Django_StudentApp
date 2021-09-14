from django.shortcuts import redirect, render
from studentapp.models import Student
from studentapp.forms import StudentForm,SignUpForm

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    context={'title':'Home'}
    return render(request,'home.html',context)


def index(request):
    std=Student.objects.order_by('-id')
    paginator=Paginator(std,8)
    page=request.GET.get('page')
    students=paginator.get_page(page)
    context={'students': students}
    return render(request,'studentapp/index.html',context)

def create_student(request):
    if request.method == "POST":
       form=StudentForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('index')
    else:
        form=StudentForm()

    context={'form':form, 'heading':'Create New Student'}
    return render(request,'studentapp/create.html',context)

def edit_student(request,id):
    if request.method == "POST":
       student=Student.objects.get(pk=id)
       form=StudentForm(request.POST or None,instance=student)
       if form.is_valid():
           form.save()
           return redirect('index')
    else:
        student=Student.objects.get(pk=id)
        form=StudentForm(request.POST or None,instance=student)
        

    context={'form':form,'title':'edit', 'heading':'Modify Student'}
    return render(request,'studentapp/create.html',context)

def delete_student(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return redirect('index')

def user_register(request):
    if request.method == "POST":
       form=SignUpForm(request.POST)
       if form.is_valid():
           user=form.save()
           user.save()
           return redirect('index')
    else:
        form=SignUpForm()

    context={'form':form,'title':'Register'}
    return render(request,'registration/register.html',context)


