from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime, timedelta

from .models import Todo
from .forms import TodoForm


@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        print form.is_valid()
        print form.errors
        if form.is_valid():
            print "hello"
            name = form.cleaned_data['name']
            print name
            description = form.cleaned_data.get('description')
            print description
            priority = form.cleaned_data.get('priority')
            state_task = form.cleaned_data.get('state_task')
            due_date = form.cleaned_data.get('due_date')
            print due_date
            if name and description and priority and state_task and due_date:
                todo_obj ,created = Todo.objects.get_or_create(
                    name=name,
                    description=description,
                    priority=priority,
                    state_task=state_task,
                    due_date=due_date
                )
                todo_obj.save()
                return HttpResponseRedirect('/todo_list/')
        return HttpResponse('ERROR IN ADDING TASK')
    form = TodoForm()
    return render(request, 'todo.html',{'form':form})


@login_required
def todo_list(request):
    if request.method == 'GET':
        print request.user
        today_date = datetime.today().date()
        todo = Todo.objects.all()
        return render(request,'index.html',{'todo':todo,'today':today_date})


@login_required
def todo_filter(request):
    if request.method == 'GET':
        date = request.GET.get('date')
        type = request.GET.get('type')
        print date, type
        colour_map = {'todo': 'blue',
                  'doing': 'red',
                  'done': 'green',
                  'expired': 'yellow'}
        if date and type == 'day_wise':
            print "in day"
            todo = Todo.objects.filter(due_date=date)
            return render(request,'index.html',{'todo':todo,'color':colour_map})
        elif date and type == 'week':
            search_date = datetime.strptime(date,'%Y-%m-%d')
            day = search_date - timedelta(days=7)
            todo = Todo.objects.filter(due_date__range=(day,date))
            return render(request,'index.html',{'todo':todo,'color':colour_map})
        elif date and type == 'month':
            search_date = datetime.strptime(date,'%Y-%m-%d')
            day = search_date - timedelta(days=7)
            print day
            todo = Todo.objects.filter(due_date__range=(day,date))
            return render(request,'index.html',{'todo':todo,'color':colour_map})
        else:
            return HttpResponse("please enter date and type to filter")


@login_required
def todo_update(request, id=None):
    if request.method == 'POST':
        instance = Todo.objects.get(id=id)
        form = TodoForm(request.POST or None, instance=instance)
        print form.errors
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data.get('description')
            priority = form.cleaned_data.get('priority')
            state_task = form.cleaned_data.get('state_task')
            due_date = form.cleaned_data.get('due_date')
        if name and description and priority and state_task and due_date:
            todo_obj = Todo.objects.get(id=id)
            todo_obj.name = name
            todo_obj.description=description
            todo_obj.priority=priority
            todo_obj.state_task=state_task
            todo_obj.due_date=due_date
            todo_obj.save()
            return HttpResponseRedirect('/todo_list/')
        return HttpResponse('ERROR IN ADDING TASK')
    instance = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=instance)
    return render(request, 'todo_update.html',{'form':form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print username
        password = request.POST.get('password')
        print password
        if username and password:
            user = authenticate(username=username,password=password)
            if user is not None:
                print "authenticated"
                login(request,user)
                return HttpResponseRedirect('/todo_list/')
            else:
                return HttpResponse("username or password doesn't match")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if username and email:
            if password1 == password2:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password1)
                user.save()
                return HttpResponseRedirect('/login/')
            return HttpResponse("password don't match")
        return HttpResponse("data is not correct")
    return render(request,'user_registration.html')
