from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

# Create your models here.

class usuarios_cliente(models.Model):
    primeiro_nome = models.CharField('Nome',max_length=120)
    sobre_nome = models.CharField('Sobrenome',max_length=120)
    cpf = models.CharField('CPF',max_length=11)
    password = models.CharField('Senha',max_length=100)

    def __str__(self):
        return self.primeiro_nome + ' ' + self.sobre_nome

class usuarios_medico(models.Model):
    primeiro_nome = models.CharField('Nome',max_length=120)
    sobre_nome = models.CharField('Sobrenome',max_length=120)
    endereco_email = models.EmailField('Endereco de email')
    password = models.CharField('Senha', max_length=100)

    def __str__(self):
        return self.primeiro_nome + ' ' + self.sobre_nome


class exames(models.Model):
    paciente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_exame = models.CharField('Exame realizado', max_length=120)
    data_realizacao = models.DateField('Data de realização do exame')
    descricao = models.TextField(blank=True)
    concluido = models.BooleanField(default=True)
    arquivo = models.FileField(upload_to="arquivos/", validators=[FileExtensionValidator(allowed_extensions=["pdf"])])

    def __str__(self):
        return self.nome_exame
