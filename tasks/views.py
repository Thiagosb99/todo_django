from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task
# Create your views here.

def list(request):
    tasks = Task.objects.all()# pegando todos o conteudo do model task (tabela no banco)
    return render(request=request, template_name='tasks/list.html', context={'tasks':tasks})

def taskView(request, id):
     task = get_object_or_404(Task, pk=id)# verifica se no model Task exist a primary key (pk) id
     return render(request=request, template_name='tasks/task.html', context={'task':task})


def yourname(request, name):
    return render(request=request, template_name='tasks/yourname.html', context={'name':name})