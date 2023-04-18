from django.urls import path

from .views import *

urlpatterns = [
    ###################################### FUNCIONARIO ######################################
    path("cadastrar/funcionario/", FuncionarioCreate.as_view(),
         name="cadastrar-funcionario"),
    path("editar/funcionario/<int:pk>/",
         FuncionarioUpdate.as_view(), name="editar-funcionario"),
    path("listar/funcionario/", FuncionarioList.as_view(),
         name="listar-funcionario"),
    path("excluir/funcionario/<int:pk>/",
         FuncionarioDelete.as_view(), name="excluir-funcionario"),
    path("detalhar/funcionario/<int:pk>/",
         FuncionarioDetail.as_view(), name="detalhar-funcionario"),

    ######################################## CLIENTE ########################################
    path("cadastrar/cliente/", ClienteCreate.as_view(), name="cadastrar-cliente"),
    path("editar/cliente/<int:pk>/",
         ClienteUpdate.as_view(), name="editar-cliente"),
    path("listar/cliente/", ClienteList.as_view(), name="listar-cliente"),
    path("excluir/cliente/<int:pk>/",
         ClienteDelete.as_view(), name="excluir-cliente"),
    path("detalhar/cliente/<int:pk>/",
         ClienteDetail.as_view(), name="detalhar-cliente"),

    ######################################## ESTADO #########################################
    path("cadastrar/estado/", EstadoCreateView.as_view(), name="cadastrar-estado"),
    path("editar/estado/<int:pk>/",
         EstadoUpdateView.as_view(), name="editar-estado"),
    path("listar/estado/", EstadoListView.as_view(), name="listar-estado"),
    path("excluir/estado/<int:pk>/",
         EstadoDeleteView.as_view(), name="excluir-estado"),
    path("detalhar/estado/<int:pk>/",
         EstadoDetailView.as_view(), name="detalhar-estado"),

    ######################################## CIDADE #########################################
    path("cadastrar/cidade/", CidadeCreateView.as_view(), name="cadastrar-cidade"),
    path("editar/cidade/<int:pk>/",
         CidadeUpdateView.as_view(), name="editar-cidade"),
    path("listar/cidade/", CidadeListView.as_view(), name="listar-cidade"),
    path("excluir/cidade/<int:pk>/",
         CidadeDeleteView.as_view(), name="excluir-cidade"),
    path("detalhar/cidade/<int:pk>/",
         CidadeDetailView.as_view(), name="detalhar-cidade"),
]
