from django.urls import path

from .views import FuncionarioCreate, FuncionarioUpdate, FuncionarioList, FuncionarioDetail, FuncionarioDelete

urlpatterns = [
    path("cadastrar/funcionario/", FuncionarioCreate.as_view(), name="cadastrar-funcionario"),
    path("editar/funcionario/<int:pk>/", FuncionarioUpdate.as_view(), name="editar-funcionario"),
    path("listar/funcionario/", FuncionarioList.as_view(), name="listar-funcionario"),
    path("excluir/funcionario/<int:pk>/", FuncionarioDelete.as_view(), name="excluir-funcionario"),
    path("detalhar/funcionario/<int:pk>/", FuncionarioDetail.as_view(), name="detalhar-funcionario"),
]