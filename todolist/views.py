from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import render
from todolist.models import Task

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


# TODO: Create your views here.
class TaskForm(forms.Form):
    title = forms.CharField(label="Judul")
    description = forms.CharField(label="Deskripsi", widget=forms.Textarea)

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user).all()
    context = {
        'list_todo': data_todolist,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def get_todolist_json(request):
    data_todolist = Task.objects.filter(user=request.user).all()
    return HttpResponse(serializers.serialize("json", data_todolist), content_type="application/json")

# def get_todolist_json_by_id(request, id):
#     data = Task.objects.filter(user=request.user, pk=id).all()
#     return HTTPResponse(serializers.serialize("json", data)

@login_required(login_url='/todolist/login/')
def add_todolist(request):
    if request.method == "POST":
        date = datetime.date.today()
        title = request.POST.get("title")
        description = request.POST.get("description")
        user = request.user

        new_todo = Task(user=user, date=date, title=title, description=description)
        new_todo.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def create_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            todo = Task(date = datetime.date.today(), 
                        title = form.cleaned_data["title"],
                        description = form.cleaned_data["description"],
                        user = request.user,)
            todo.save()
            messages.success(request, "Task Berhasil Disimpan")
            return redirect("todolist:show_todolist")
    form = TaskForm()
    context = {"form": form}
    return render(request, "create.html", context)