from django.db import models

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


class Servico(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} ({self.descricao})"


class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    dataAgendamento = models.DateTimeField()
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    horario = models.TimeField(verbose_name="Horário")

    def __str__(self):
        return f"{self.cliente} ({self.horario})"
