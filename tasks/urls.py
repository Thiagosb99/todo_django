from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.list, name='list'),
    path('yourname/<str:name>', views.yourname, name='yourname')
    #passar parametro é <tipo de dado: e nome parametro
]
