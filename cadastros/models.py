from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14)
    observacao = models.CharField(max_length=100, null=True, verbose_name="Observação")
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.nome} ({self.telefone})"
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14)
    observacao = models.CharField(max_length=100, null=True, verbose_name="Observação")

    def __str__(self) :
        return f"{self.nome} ({self.telefone})"
    
class Servico(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) :
        return f"{self.nome} ({self.descricao})"
    
class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    horario = models.TimeField(verbose_name="Horário")

    def __str__(self) :
        return f"{self.cliente} ({self.horario})"