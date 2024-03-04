from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .form import Taskform

# Create your views here.
def task_list(request):
    tasks=Task.objects.all()
    return render(request,'task_list.html',{'tasks':tasks})

def task_detail(request,id):
    task=get_object_or_404(Task,id=id)
    return render(request,'task_details.html')
def create_task(request):
    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            form=Taskform()
        return render(request,'task_form.html',{'form':form})

def edit_task(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=='POST':
        form=Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            form=Taskform(instance=task)
        return render(request,'task_form.html')
def delete_task(request,id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('')
    return render(request,'task_confirm_delete.html')
        

