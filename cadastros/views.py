from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

# Create your views here.


class SobreView(TemplateView):
    template_name = "cadastros/list/sobre.html"

#################### CADASTRAR ####################


class FuncionarioCreate(LoginRequiredMixin, CreateView):
    model = Funcionario
    fields = ["nome", "cpf", "telefone", "endereco",
              "numero", "cep", "bairro", "email",  "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Funcionarios"
        return dados


class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ["nome", "endereco", "telefone", "email", "cpf", "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Clientes"
        return dados


class EstadoCreateView(LoginRequiredMixin, CreateView):
    model = Estado
    fields = ["nome", "sigla"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estado")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Estados"
        return dados


class CidadeCreateView(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ["nome", "estado"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cidade")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Cidades"
        return dados


class EmpresaCreateView(LoginRequiredMixin, CreateView):
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


class FuncionarioUpdate(LoginRequiredMixin, UpdateView):
    model = Funcionario
    fields = ["nome", "endereco", "telefone", "email", "cpf", "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ["nome", "endereco", "telefone", "email", "cpf", "observacao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")


class EstadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Estado
    fields = ["nome", "sigla"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estado")


class CidadeUpdateView(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ["nome", "estado"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cidade")


class EmpresaUpdateView(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = ["nome", "cnpj", "telefone", "endereco", "numero", "cep", "bairro",
              "logo", "data_cadastro", "horario_abertura", "horario_fechamento"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")


#################### DELETAR ####################


class FuncionarioDelete(LoginRequiredMixin, DeleteView):
    model = Funcionario
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")


class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")


class EstadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Estado
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estado")


class CidadeDeleteView(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cidade")


class EmpresaDeleteView(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")

#################### LISTAR ####################


class FuncionarioList(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = "cadastros/list/funcionario.html"


class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "cadastros/list/cliente.html"


class EstadoListView(LoginRequiredMixin, ListView):
    model = Estado
    template_name = "cadastros/list/estado.html"


class CidadeListView(LoginRequiredMixin, ListView):
    model = Cidade
    template_name = "cadastros/list/cidade.html"


class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = "cadastros/list/empresa.html"

#################### DETALHES ####################


class FuncionarioDetail(LoginRequiredMixin, DetailView):
    model = Funcionario
    template_name = "cadastros/detail/funcionario.html"


class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = "cadastros/detail/cliente.html"


class EstadoDetailView(LoginRequiredMixin, DetailView):
    model = Estado
    template_name = "cadastros/detail/estado.html"


class CidadeDetailView(LoginRequiredMixin, DetailView):
    model = Cidade
    template_name = "cadastros/detail/cidade.html"


class EmpresaDetailView(LoginRequiredMixin, DetailView):
    model = Empresa
    template_name = "cadastros/detail/empresa.html"
