from .models import Funcionario
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


#################### CADASTRAR ####################
class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")

#################### ATUALIZAR ####################

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-funcionario")

#################### DELETAR ####################

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-funcionario")

#################### LISTAR ####################

class FuncionarioList(ListView):
    model = Funcionario
    template_name = "cadastros/list/funcionario.html"

#################### DETALHES ####################

class FuncionarioDetail(DetailView):
    model = Funcionario
    template_name = "cadastros/detail/funcionario.html"