from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from forms import GroupForm
from django.urls import reverse
from mainapp.models import Group


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def group_list(request):
    group = Group.objects.all()
    context = {
        'title': 'группы',
        'group': group,
    }
    return render(request, 'mainapp/group_all', context)

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Группа добавлена')
            return HttpResponseRedirect(reverse('mainapp:'))
