from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.list, name='list'),
    path('task/<int:id>', views.taskView, name='task_view'),
    path('yourname/<str:name>', views.yourname, name='yourname')
    #passar parametro é <tipo de dado: e nome parametro
]
