from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

def list(request):
    tasks = Task.objects.all().order_by('-create_at')# pegando todos o conteudo do model task (tabela no banco) e ordenado pela data de criação 
    return render(request=request, template_name='tasks/list.html', context={'tasks':tasks})

def taskView(request, id):
     task = get_object_or_404(Task, pk=id)# verifica se no model Task exist a primary key (pk) id
     return render(request=request, template_name='tasks/task.html', context={'task':task})


def newTask(request):

    if request.method == 'POST': #se methodo na url for post 
        form = TaskForm(request.POST) # pega os dados via post enviados pra essa view

        if form.is_valid(): # valida esses dados
            # form.save() salva os dados no banco (commit = False) = para esse salvamento de dados até mandarmos salvar novamente
            #nesse meio tempo onde ainda não foi mandado salvar novamente é possivel fazer modificações 
            # nessa caso eu atualizo o campo 'done' da tabela pra doing e depois salvo no banco com essa nova alteração 
            task = form.save(commit=False) 
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()#pega a classe do form que foi criada para inserir dados no banco via form
        return render(request=request, template_name='tasks/addtask.html', context={'form':form})

def yourname(request, name):
    return render(request=request, template_name='tasks/yourname.html', context={'name':name})