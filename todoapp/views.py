from django.shortcuts import render,redirect
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            form.save()
        messages.success(request,("New Task Added Successfully!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)
        return render(request,'task.html',{'all_tasks':all_tasks})

@login_required
def delete_task(request,id):
    task = TaskList.objects.get(id=id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, ("Access Restricted!"))
    return redirect('todolist')

@login_required
def edit_task(request,id):
    if request.method == 'POST':
        task = TaskList.objects.get(id=id)
        form = TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited Successfully!"))
        return redirect('todolist')
    else:
        task = TaskList.objects.get(id=id)
        return render(request,'edit.html',{'task':task})

@login_required
def complete_task(request,id):
    task = TaskList.objects.get(id=id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Access Restricted!"))
    return redirect('todolist')

@login_required
def pending_task(request,id):
    task = TaskList.objects.get(id=id)
    task.done = False
    task.save()
    return redirect('todolist')

def about(request):
    context = {
        'welcome_msg': "About Us"
    }
    return render(request,'about.html',context)

def index(request):
    context = {
        'welcome_msg': "Welcome to TaskMaster!"
    }
    return render(request,'index.html',context)

def contact(request):
    context = {
        'welcome_msg': "Contact Us"
    }
    return render(request,'contact.html',context)