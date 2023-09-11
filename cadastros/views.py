from django.http import HttpResponseRedirect
from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from .models import *
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

# Importação da biblioteca do autocomplete
from dal import autocomplete

# Importação dos meus formulários personalizados
from .forms import EmpresaForm

# Create your views here.



class SobreView(TemplateView):
    template_name = "cadastros/list/sobre.html"

#################### CADASTRAR ####################


class FuncionarioCreate(GroupRequiredMixin, CreateView):
    model = Funcionario
    fields = ["nome", "cpf", "telefone", "endereco",
              "numero", "cep", "bairro", "email", "usuario", "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")
    group_required = ["Administrador"]

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Funcionarios"
        return dados


class ClienteCreate(GroupRequiredMixin, CreateView):
    model = Cliente
    fields = ["nome", "endereco", "telefone",
              "email", "cpf", "usuario", "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")
    group_required = ["Administrador"]

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Clientes"
        return dados


class EstadoCreateView(GroupRequiredMixin, CreateView):
    model = Estado
    fields = ["nome", "sigla"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estado")
    group_required = ["Administrador"]

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Estados"
        return dados


class CidadeCreateView(GroupRequiredMixin, CreateView):
    model = Cidade
    fields = ["nome", "estado"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cidade")
    group_required = ["Administrador"]

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Cidades"
        return dados


class EmpresaCreateView(GroupRequiredMixin, CreateView):
    form_class = EmpresaForm
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")
    group_required = ["Administrador"]

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Empresas"
        return dados

class ServicoCreateView(GroupRequiredMixin, CreateView):
    model = Servico
    fields = ["nome", "descricao", "valor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-servico")
    group_required = ["Administrador"]

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Serviço"
        return dados

class AgendamentoCreateView(GroupRequiredMixin, CreateView):
    model = Agendamento
    fields = ["cliente", "data_agendamento", "servico", "horario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-agendamento")
    group_required = ["Administrador"]

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Agendamento"
        return dados

#################### ATUALIZAR ####################


class FuncionarioUpdate(GroupRequiredMixin, UpdateView):
    model = Funcionario
    fields = ["nome", "endereco", "telefone",
              "email", "cpf", "usuario", "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")
    group_required = ["Administrador"]


class ClienteUpdate(GroupRequiredMixin, UpdateView):
    model = Cliente
    fields = ["nome", "endereco", "telefone",
              "email", "cpf", "usuario", "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")
    group_required = ["Administrador"]


class EstadoUpdateView(GroupRequiredMixin, UpdateView):
    model = Estado
    fields = ["nome", "sigla"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estado")
    group_required = ["Administrador"]


class CidadeUpdateView(GroupRequiredMixin, UpdateView):
    model = Cidade
    fields = ["nome", "estado"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cidade")
    group_required = ["Administrador"]


class EmpresaUpdateView(GroupRequiredMixin, UpdateView):
    model = Empresa
    fields = ["nome", "cnpj", "telefone", "endereco", "numero", "cep", "bairro",
              "logo", "data_cadastro", "horario_abertura", "horario_fechamento", "funcionario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")
    group_required = ["Administrador"]

class ServicoUpdateView(GroupRequiredMixin, UpdateView):
    model = Servico
    fields = ["nome", "descricao", "valor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-servico")
    group_required = ["Administrador"]

class AgendamentoUpdateView(GroupRequiredMixin, UpdateView):
    model = Agendamento
    fields = ["cliente", "data_agendamento", "servico", "horario"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-agendamento")
    group_required = ["Administrador"]

#################### DELETAR ####################


class FuncionarioDelete(GroupRequiredMixin, DeleteView):
    model = Funcionario
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")
    group_required = ["Administrador"]


class ClienteDelete(GroupRequiredMixin, DeleteView):
    model = Cliente
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")
    group_required = ["Administrador"]


class EstadoDeleteView(GroupRequiredMixin, DeleteView):
    model = Estado
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estado")
    group_required = ["Administrador"]


class CidadeDeleteView(GroupRequiredMixin, DeleteView):
    model = Cidade
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cidade")
    group_required = ["Administrador"]


class EmpresaDeleteView(GroupRequiredMixin, DeleteView):
    model = Empresa
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")
    group_required = ["Administrador"]

class ServicoDeleteView(GroupRequiredMixin, DeleteView):
    model = Servico
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-servico")
    group_required = ["Administrador"]

class AgendamentoDeleteView(GroupRequiredMixin, DeleteView):
    model = Agendamento
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-agendamento")
    group_required = ["Administrador"]

#################### LISTAR ####################


class FuncionarioList(GroupRequiredMixin, ListView):
    model = Funcionario
    template_name = "cadastros/list/funcionario.html"
    group_required = ["Administrador"]
    paginate_by = 50

    def get_queryset(self):
        self.object_list = Funcionario.objects.all().select_related("usuario")
        return self.object_list


class ClienteList(GroupRequiredMixin, ListView):
    model = Cliente
    template_name = "cadastros/list/cliente.html"
    group_required = ["Administrador"]
    paginate_by = 50

    def get_queryset(self):
        self.object_list = Cliente.objects.all().select_related("usuario")
        return self.object_list


class EstadoList(GroupRequiredMixin, ListView):
    model = Estado
    template_name = "cadastros/list/estado.html"
    group_required = ["Administrador"]
    paginate_by = 50


class CidadeList(GroupRequiredMixin, ListView):
    model = Cidade
    template_name = "cadastros/list/cidade.html"
    group_required = ["Administrador"]
    paginate_by = 50

    def get_queryset(self):
        self.object_list = Cidade.objects.all().select_related("estado")
        return self.object_list


class EmpresaList(GroupRequiredMixin, ListView):
    model = Empresa
    template_name = "cadastros/list/empresa.html"
    group_required = ["Administrador"]
    paginate_by = 50

    def get_queryset(self):
        self.object_list = Empresa.objects.all().select_related("cidade", "funcionario")
        return self.object_list

class ServicoList(GroupRequiredMixin, ListView):
    model = Servico
    template_name = "cadastros/list/servico.html"
    group_required = ["Administrador"]
    paginate_by = 50

class AgendamentoList(GroupRequiredMixin, ListView):
    model = Agendamento
    template_name = "cadastros/list/agendamento.html"
    group_required = ["Administrador"]
    paginate_by = 50

    def get_queryset(self):
        self.object_list = Agendamento.objects.all().select_related("cliente", "servico")
        return self.object_list

#################### DETALHES ####################


class FuncionarioDetail(GroupRequiredMixin, DetailView):
    model = Funcionario
    template_name = "cadastros/detail/funcionario.html"
    group_required = ["Administrador"]


class ClienteDetail(GroupRequiredMixin, DetailView):
    model = Cliente
    template_name = "cadastros/detail/cliente.html"
    group_required = ["Administrador"]


class EstadoDetailView(GroupRequiredMixin, DetailView):
    model = Estado
    template_name = "cadastros/detail/estado.html"
    group_required = ["Administrador"]


class CidadeDetailView(GroupRequiredMixin, DetailView):
    model = Cidade
    template_name = "cadastros/detail/cidade.html"
    group_required = ["Administrador"]


class EmpresaDetailView(GroupRequiredMixin, DetailView):
    model = Empresa
    template_name = "cadastros/detail/empresa.html"
    group_required = ["Administrador"]

class ServicoDetailView(GroupRequiredMixin, DetailView):
    model = Servico
    template_name = "cadastros/detail/servico.html"
    group_required = ["Administrador"]

class AgendamentoDetailView(GroupRequiredMixin, DetailView):
    model = Agendamento
    template_name = "cadastros/detail/agendamento.html"
    group_required = ["Administrador"]

############## AUTOCOMPLETE ################

# Criar uma view com essa herança e que retorne uma lista de objetos
class FuncionarioAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        object_list = Funcionario.objects.all()

        # Pega o termo do campo e faz um filtro nele
        if self.q:
            object_list = object_list.filter(
                nome__icontains=self.q
            )
        # Retorna a lista de objetos
        return object_list