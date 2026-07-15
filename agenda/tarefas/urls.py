from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('concluir/<int:id>/', views.concluir_tarefa, name='concluir_tarefa'),
    path('editar<int:id>/', views.editar_tarefa, name='editar_tarefa'),
]