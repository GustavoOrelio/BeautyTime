from django.contrib import admin
from .models import Cliente, Funcionario, Agendamento, Servico

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Agendamento)
admin.site.register(Servico)