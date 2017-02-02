from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView, ListView
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

from .models import TodoList


def to_do_list_index(requset):
    if requset.user.is_authenticated():
        complete_tasks = TodoList.objects.filter(user=requset.user, state=True).order_by('-pk')
        uncomplete_tasks = TodoList.objects.filter(user=requset.user, state=False).order_by('-pk')
        content = {
            'completed_tasks': complete_tasks,
            'uncompleted_tasks': uncomplete_tasks
        }
        return render(requset, 'todolist/index.html', content)
    else:
        return render(requset, 'todolist/index.html')


class AddTaskView(TemplateView):
    template_name = 'todolist/add-task.html'


def create_task(request):
    task = request.POST['task']
    remark = None
    if request.POST['remark']:
        remark = request.POST['remark']
    to_do = TodoList(user=request.user, task=task, remark=remark)
    to_do.save()
    return redirect('todolistindex')


def delete_task(request, pk):
    TodoList.objects.get(pk=pk).delete()
    return redirect('todolistindex')


def complete_task(request):
    to_do = TodoList.objects.get(pk=request.GET['pk'])
    to_do.state = True
    to_do.completed_time = timezone.now()
    to_do.save()
    return HttpResponse()


def uncomplete_task(request):
    to_do = TodoList.objects.get(pk=request.GET['pk'])
    to_do.state = False
    to_do.completed_time = None
    to_do.save()
    return HttpResponse()


class SignInView(TemplateView):
    template_name = 'todolist/sign-in.html'


def login_to_to_do_list(request):
    username = request.POST['name']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user and user.is_active:
            login(request, user)
    return redirect('todolistindex')


def logout_off_to_do_list(request):
    logout(request)
    return redirect('todolistindex')
