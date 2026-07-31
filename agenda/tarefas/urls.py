from django.urls import path
from . import views
from .views import LoginUsuario
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path("login/", LoginUsuario.as_view(), name="login"),
    path("logout/SS", LogoutView.as_view(next_page="login"), name="logout"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('concluir/<int:id>/', views.concluir_tarefa, name='concluir_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
]