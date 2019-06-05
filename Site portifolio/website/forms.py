from django import forms
from django.core.mail import send_mail

class ContatoForm(forms.Form):
    ASSUNTOS = (
        ('B','Bug'),
        ('R','Reclamação'),
        ('S','Sugestão')
    )
    RESPOSTAS = (
        ('T','Telefone'),
        ('E','E-mail')
    )

    nome = forms.CharField(required=True, max_length=120)
    email = forms.EmailField(required=False)
    telefone = forms.CharField(required=False)
    mensagem = forms.CharField(required=True)
    assunto = forms.ChoiceField(choices=ASSUNTOS, required=True)
    resposta = forms.MultipleChoiceField(choices=RESPOSTAS, required=False)

    def clean(self):
        dados = self.cleaned_data
        email = dados['email']
        telefone = dados['telefone']
        respostas = dados['resposta']
        if 'E' in respostas and not email:
            self.add_error(None, 'E-mail é obrigatório quando for escolhido como resposta')
        if 'T' in respostas and not telefone:
            self.add_error(None, 'Telefone é obrigatório quando for escolhido como resposta.')



    def enviar_email(self):
        nome = self.cleaned_data['nome']
        telefone = self.cleaned_data['telefone']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        email = self.cleaned_data['email']

        print('ENVIANDO:',self.cleaned_data)

        resposta_email = ''
        if self.is_valid():
            respostas = self.cleaned_data['resposta']
            for resp in respostas:
                resposta_email += 'E-mail;' if resp == 'E' else 'Telefone;'

        mensagem_email = 'Você recebeu o contato do seguinte usuário:\n'\
            '->Nome: '+nome+'\n'\
            '->E-mail: '+email+'\n'\
            '->Telefone: '+telefone+'\n'\
            '->Assunto: '+self.formatar_assunto(assunto) +'\n'\
            '->Resposta: '+resposta_email+'\n'\
            '->Mensagem: '+mensagem


        print(mensagem_email)
        
        send_mail(
            f'FIT Contato - {self.formatar_assunto(assunto)}',
            mensagem_email,
            email,
            ['contato@fit.com.br']
        )

    def formatar_assunto(self, assunto) -> str:
        if assunto == 'B':
            assunto = 'Bug'
        elif assunto == 'R':
            assunto = 'Reclamação'
        else:
            assunto = 'Sugestão'
        return assunto
        