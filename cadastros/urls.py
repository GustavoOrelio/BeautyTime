from django.urls import path

from .views import FuncionarioCreate, FuncionarioUpdate, FuncionarioList, FuncionarioDetail, FuncionarioDelete
from .views import ClienteCreate, ClienteUpdate, ClienteList, ClienteDetail, ClienteDelete

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
]
