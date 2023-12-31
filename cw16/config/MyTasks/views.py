from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib import messages
from .mixins import *
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView


def home(request):
    tasks = Task.objects.order_by('due_date')

    return render(request, 'MyTasks/home.html', {'tasks': tasks})


class AllTasksListView(ListView):
    model = Task
    template_name = 'MyTasks/alltasks.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'MyTasks/details.html'
    context_object_name = 'task'
    pk_url_kwarg = 'pk'


def see_user_tasks(request, user):
    all_user_tasks = get_list_or_404(Task, user=user)
    return render(request, 'MyTasks/user_tasks.html', {'all_user_tasks': all_user_tasks})


class TaskUpdateView(UpdateView):
    form_class = MyTaskForm
    model = Task
    pk_url_kwarg = 'id'
    template_name = 'MyTasks/update.html'

    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)

# def update_task(request,pk):
#     task=get_object_or_404(Task,id=pk)
#     if request.method=='POST':
#         form=MyTaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Content has been chaged','success')
#             return redirect('MyTasks/details.html',id)
#     else:
#         task=MyTaskForm(request, instance=task)
#         context={'task':task}
#         return render(request, 'MyTasks/update.html', context)


def search(request):
    return render(request, 'MyTasks/search.html')


def search_result(request):
    if request.method == 'POST':
        word = request.POST.get('search')
        task = Task.objects.filter(
            Q(title__icontains=word) & Q(description__icontains=word))
    return render(request, 'MyTasks/result.html', {'task': task})


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'MyTasks/taskform.html'

    def form_valid(self, form):
        return super().form_valid(form)

# @login_required(login_url='login')
# def create_task(request):
#     if request.method=='POST':
#         form=TaskForm(request.POST)
#         if form.is_valid():
#             cd=form.cleaned_data
#             Task.objects.create(title=cd['title'], description=cd['description'], due_date=cd['due_date']
#                                 , tags=cd['tags'], status_field=cd['status_field'])
#     else:
#         form=TaskForm()
#     return render(request, 'MyTasks/taskform.html', {'form': form})


class ProfileView(ProfileMixin, View):
    template_name = 'MyTasks/profile.html'

# class TodoUpdateView(TodoOwnerRequiredMixin, View):
#     template_name="MyTasks/update.html"
