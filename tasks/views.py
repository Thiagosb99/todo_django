from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task # importa o model task
from .forms import TaskForm # importa o form taskform
from django.contrib import messages # messagens de retorndo de sucesso or fail essas paradas
# Create your views here.

def list(request):# request é sempre padrao ns funcoes das views
    tasks = Task.objects.all().order_by('-create_at')# pegando todos o conteudo do model task (tabela no banco) e ordenado pela data de criação 
    return render(request=request, template_name='tasks/list.html', context={'tasks':tasks})

def taskView(request, id):
     task = get_object_or_404(Task, pk=id)# verifica se no model Task exist a primary key (pk) id
     return render(request=request, template_name='tasks/task.html', context={'task':task})


def newTask(request):
    #o django nao precisa informa se a funcao sera para get ou post ele carrega a pagina do mesmo jeito
    #caso seja post que verifico em baixo e faço a insercao de dados vindos do post no banco de dados

    if request.method == 'POST': #se methodo na url for post 
        form = TaskForm(request.POST) # pega os dados via post enviados pra essa view

        if form.is_valid(): # valida esses dados
            # form.save() salva os dados no banco (commit = False) = para esse salvamento de dados até mandarmos salvar novamente
            #nesse meio tempo onde ainda não foi mandado salvar novamente é possivel fazer modificações 
            # nessa caso eu atualizo o campo 'done' da tabela pra doing e depois salvo no banco com essa nova alteração 
            task = form.save(commit=False) 
            task.done = 'doing'
            task.save()
            messages.success(request=request, message="Tarefa adicionada com Sucesso!")
            return redirect('/')
    else:
        form = TaskForm()#pega a classe do form que foi criada para inserir dados no banco via form
        return render(request=request, template_name='tasks/addtask.html', context={'form':form})


def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task) # pega os dados com form com os dados puxados anteriormentes do banco atraves do object_or_40

    if(request.method == "POST"):
        form = TaskForm(request.POST, instance= task)#faz a mesma coisa que em cima
        if form.is_valid():
            task.save()
            messages.success(request=request, message="Tarefa editada com Sucesso!")
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form':form, 'task':task})

    else:
        return render(request, 'tasks/edittask.html', {'form':form, 'task':task})

def deleteTask(request, id):
    try:
        task = get_object_or_404(Task, pk=id)#acha no model task o id do dado especifico
        task.delete()#deleta esse dado do banco de dados

        messages.success(request=request, message="Tarefa deletada com Sucesso!")
        return redirect('/')
    except:
        messages.error(request=request, message="Ocorreu algum erro")
        return redirect('/')


def yourname(request, name):
    return render(request=request, template_name='tasks/yourname.html', context={'name':name})