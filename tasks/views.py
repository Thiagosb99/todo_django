from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def list(request):
    return render(request=request, template_name='tasks/list.html')

def yourname(request, name):
    return render(request=request, template_name='tasks/yourname.html', context={'name':name})