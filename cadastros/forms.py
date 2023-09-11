from dal import autocomplete
from django import forms
from .models import Empresa


class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = [
            'nome', 'cnpj', 'telefone', 'endereco', 'numero', 'cep', 'bairro', 'logo',
            'data_cadastro', 'horario_abertura', 'horario_fechamento', 'cidade', 'funcionario'
        ]
        widgets = {
            
            # O campo 'funcionario' vai usar a seguinte URL para montar o campo
            # e fazer o filtro com base no que foi digitado
            'funcionario' : autocomplete.ModelSelect2Multiple(
                url='buscar-funcionario',
                attrs={
                    'data-placeholder': 'Informe o nome do funcionario...',
                }, # Fim do attrs
            ),  # Fim do autocomplete.ModelSelect2()

        } # Fim do widgets
