from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.list, name='list'),
    path('task/<int:id>', views.taskView, name='task_view'),
    #passar parametro é <tipo de dado: e nome parametro
    path("newtask/", views.newTask, name="new_task"),
    path("edittask/<int:id>", views.editTask, name="edit_task"),
    path("deletetask/<int:id>", views.deleteTask, name="delete_task"),

]
