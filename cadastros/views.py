from .models import Funcionario, Cliente
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


#################### CADASTRAR ####################
class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ["nome", "cpf", "telefone", "endereco",
              "numero", "cep", "bairro", "email",  "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Funcionarios"
        return dados


class ClienteCreate(CreateView):
    model = Cliente
    fields = ["nome", "endereco", "telefone", "email", "cpf", "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")


#################### ATUALIZAR ####################

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ["nome", "endereco", "telefone", "email", "cpf", "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ["nome", "endereco", "telefone", "email", "cpf", "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")

#################### DELETAR ####################


class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-funcionario")


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-cliente")

#################### LISTAR ####################


class FuncionarioList(ListView):
    model = Funcionario
    template_name = "cadastros/list/funcionario.html"


class ClienteList(ListView):
    model = Cliente
    template_name = "cadastros/list/cliente.html"

#################### DETALHES ####################


class FuncionarioDetail(DetailView):
    model = Funcionario
    template_name = "cadastros/detail/funcionario.html"


class ClienteDetail(DetailView):
    model = Cliente
    template_name = "cadastros/detail/cliente.html"
