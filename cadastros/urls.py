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
    path("listar/estado/", EstadoList.as_view(), name="listar-estado"),
    path("excluir/estado/<int:pk>/",
         EstadoDeleteView.as_view(), name="excluir-estado"),
    path("detalhar/estado/<int:pk>/",
         EstadoDetailView.as_view(), name="detalhar-estado"),

    ######################################## CIDADE #########################################
    path("cadastrar/cidade/", CidadeCreateView.as_view(), name="cadastrar-cidade"),
    path("editar/cidade/<int:pk>/",
         CidadeUpdateView.as_view(), name="editar-cidade"),
    path("listar/cidade/", CidadeList.as_view(), name="listar-cidade"),
    path("excluir/cidade/<int:pk>/",
         CidadeDeleteView.as_view(), name="excluir-cidade"),
    path("detalhar/cidade/<int:pk>/",
         CidadeDetailView.as_view(), name="detalhar-cidade"),

    ######################################## EMPRESA #########################################
    path("cadastrar/empresa/", EmpresaCreateView.as_view(), name="cadastrar-empresa"),
    path("editar/empresa/<int:pk>/",
         EmpresaUpdateView.as_view(), name="editar-empresa"),
    path("listar/empresa/", EmpresaList.as_view(), name="listar-empresa"),
    path("excluir/empresa/<int:pk>/",
         EmpresaDeleteView.as_view(), name="excluir-empresa"),
    path("detalhar/empresa/<int:pk>/",
         EmpresaDetailView.as_view(), name="detalhar-empresa"),

     ######################################## SERVIÇO #########################################
    path("cadastrar/servico/", ServicoCreateView.as_view(), name="cadastrar-servico"),
    path("editar/servico/<int:pk>/",
         ServicoUpdateView.as_view(), name="editar-servico"),
    path("listar/servico/", ServicoList.as_view(), name="listar-servico"),
    path("excluir/servico/<int:pk>/",
         ServicoDeleteView.as_view(), name="excluir-servico"),
    path("detalhar/servico/<int:pk>/",
         ServicoDetailView.as_view(), name="detalhar-servico"),

     ######################################## AGENDAMENTO #########################################
     path("cadastrar/agendamento/", AgendamentoCreateView.as_view(), name="cadastrar-agendamento"),
     path("editar/agendamento/<int:pk>/",
         AgendamentoUpdateView.as_view(), name="editar-agendamento"),
     path("listar/agendamento/", AgendamentoList.as_view(), name="listar-agendamento"),
     path("excluir/agendamento/<int:pk>/",
         AgendamentoDeleteView.as_view(), name="excluir-agendamento"),
     path("detalhar/agendamento/<int:pk>/",
         AgendamentoDetailView.as_view(), name="detalhar-agendamento"),

     # URL do autocomplete
     path("buscar/funcionario/", FuncionarioAutocomplete.as_view(), name="buscar-funcionario"),

     path("sobre/", SobreView.as_view(), name="sobre"),
]
