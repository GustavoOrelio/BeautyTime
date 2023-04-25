from django.http import HttpResponseRedirect
from .models import *
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


class EstadoCreateView(CreateView):
    model = Estado
    fields = ["nome", "sigla"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estado")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Estados"
        return dados


class CidadeCreateView(CreateView):
    model = Cidade
    fields = ["nome", "estado"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cidade")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Cidades"
        return dados


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ["nome", "cnpj", "telefone", "endereco", "numero", "cep", "bairro",
              "logo", "data_cadastro", "horario_abertura", "horario_fechamento"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Empresas"
        return dados

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


class EstadoUpdateView(UpdateView):
    model = Estado
    fields = ["nome", "sigla"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estado")


class CidadeUpdateView(UpdateView):
    model = Cidade
    fields = ["nome", "estado"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cidade")


class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = ["nome", "cnpj", "telefone", "endereco", "numero", "cep", "bairro",
              "logo", "data_cadastro", "horario_abertura", "horario_fechamento"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")


#################### DELETAR ####################


class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")


class EstadoDeleteView(DeleteView):
    model = Estado
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estado")


class CidadeDeleteView(DeleteView):
    model = Cidade
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cidade")


class EmpresaDeleteView(DeleteView):
    model = Empresa
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")

#################### LISTAR ####################


class FuncionarioList(ListView):
    model = Funcionario
    template_name = "cadastros/list/funcionario.html"


class ClienteList(ListView):
    model = Cliente
    template_name = "cadastros/list/cliente.html"


class EstadoListView(ListView):
    model = Estado
    template_name = "cadastros/list/estado.html"


class CidadeListView(ListView):
    model = Cidade
    template_name = "cadastros/list/cidade.html"


class EmpresaListView(ListView):
    model = Empresa
    template_name = "cadastros/list/empresa.html"

#################### DETALHES ####################


class FuncionarioDetail(DetailView):
    model = Funcionario
    template_name = "cadastros/detail/funcionario.html"


class ClienteDetail(DetailView):
    model = Cliente
    template_name = "cadastros/detail/cliente.html"


class EstadoDetailView(DetailView):
    model = Estado
    template_name = "cadastros/detail/estado.html"


class CidadeDetailView(DetailView):
    model = Cidade
    template_name = "cadastros/detail/cidade.html"


class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = "cadastros/detail/empresa.html"
