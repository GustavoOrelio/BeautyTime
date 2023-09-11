from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    numero = models.CharField(max_length=5, verbose_name="Número residencial")
    cep = models.CharField(max_length=9, verbose_name="CEP")
    bairro = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    observacao = models.CharField(
        max_length=100, null=True, verbose_name="Observação")
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.telefone})"


class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    numero = models.CharField(max_length=5, verbose_name="Número residencial")
    cep = models.CharField(max_length=9, verbose_name="CEP")
    bairro = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    observacao = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Observação")
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.telefone})"


class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.estado.sigla})"


class Empresa(models.Model):
    
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=8)
    bairro = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="", null=True, blank=True)
    data_cadastro = models.DateField()
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    funcionario = models.ManyToManyField(Funcionario)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} ({self.descricao})"


class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    dataAgendamento = models.DateField(verbose_name="Data de Agendamento")
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    horario = models.TimeField(verbose_name="Horário")

    def __str__(self):
        return f"{self.cliente} ({self.horario})"
