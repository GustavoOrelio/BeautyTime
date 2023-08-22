from django.views.generic import TemplateView
from cadastros.models import Agendamento
from datetime import datetime

class IndexView(TemplateView):
    template_name = "paginas/index.html"

    def get_context_data (self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["agendamento"] = Agendamento.objects.filter(dataAgendamento__gte = datetime.today()).order_by("dataAgendamento").select_related("cliente", "servico")
        return dados