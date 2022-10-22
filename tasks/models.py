from pyexpat import model
from random import choices
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models


#aqui onde a gente cria o model que equivale a tabela no banco de dados, seguindo a syntaxe do django

#apos configurado o model comandos pra rodar

#python manage.py makemigrations - gera a migrations no django
#python manage.py miigrate - cria a tabela no banco
#python manage.py createsuperuser - cria um usuario super admin para gerenciar os dados do banco pelo proprio django mesmo, uma tela de administcao acessado pela /admin no browser

class Task(models.Model):

    STATUS=(
       ('doing', 'Doing'),
       ('done', 'Done'), 
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length = 5, choices = STATUS)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
