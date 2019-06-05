from django import forms
from django.core.mail import send_mail
from .data import USUARIOS

class InscreverForm(forms.Form):
    SEXOS = (
        ('M','Masculino'),
        ('F','Feminino')
    )
    usuario = forms.CharField(required=True, min_length=5, max_length=10)
    senha = forms.CharField(required=True)
    confirmacao_senha = forms.CharField(required=True)
    nome = forms.CharField(min_length=5, max_length=100, required=True)
    email = forms.EmailField(required=True)
    celular = forms.CharField(required=False)
    sexo = forms.ChoiceField(choices=SEXOS, required=True)
    cor = forms.CharField(required=False)
    github = forms.URLField(required=False)

    def clean(self):
        dados = self.cleaned_data
        print(dados)
        if self.is_valid():
            if dados['senha'] != dados['confirmacao_senha']:
                self.add_error(None, 'Senhas devem ser iguais!')


class EntrarForm(forms.Form):
    usuario = forms.CharField(required=True, min_length=5, max_length=10)
    senha = forms.CharField(required=True)

    def clean(self):
        self.autenticar()
        print("AUTENTICADO? = ",self.autenticar())

    def autenticar(self) -> bool:
        if self.is_valid():
            usuario = self.cleaned_data['usuario']
            senha = self.cleaned_data['senha']
            for user in USUARIOS:
                if usuario == user['usuario'] and senha == user['senha']:
                    return True
                else:
                    self.add_error(None,'Usuário ou senha incorretos!')
                    return False


class EsqueciForm(forms.Form):

    email = forms.EmailField(required=True)

    def clean(self):
        self.enviar_senha()

    def enviar_senha(self):
        email = self.cleaned_data['email']
        for user in USUARIOS:
            if email == user['email']:
                senha = user['senha']
                send_mail('FIT Contato - Lembre de Senha', f'A senha do seu usuário é {senha}', user['email'],['contato@fit.com.br'])
                return
        self.add_error(None,'E-mail não cadastrado!')
        
                

class LembrarForm(forms.Form):

    senha = forms.CharField()
    confirmar_senha = forms.CharField()

    def salvar_senha(self):
        senha = self.cleaned_data.get("senha")
        senha2 = self.cleaned_data.get("confirmar_senha")

        if senha != senha2:
            self.add_error(None, "Senhas devem ser iguais!")