from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Pessoa(models.Model):
    SEXO_CHOICES = (("M", "Masculino"), ("F", "Feminino"))
   
    nome = models.CharField(max_length=11, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    genero = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    
    def __str__(self):
     return self.nome

    class Funcionario(Pessoa):
     TURNO_CHOICES = (('M', 'Manhã'),('T', 'Tarde'),('N', 'Noite'),
)
     
     matricula = models.CharField(max_length=5, blank=False, null=False)
     cargo = models.CharField(max_length=256, blank=False, null=False)
     turno = models.CharField(max_length=1, choices=TURNO_CHOICES, blank=False, null=False)
     usuario = models.OneToOneField(User, related_name= 'funcionario', on_delete=models.CASCADE)
     
     class Visitante(Pessoa):
         TIPO_CHOICES = (('E', 'Escola'),('D','Delivery'),('V', 'Visitante'),)
         
         tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=False, null=False)
         
    class Endereco(models.Model):
        logradouro = models.CharField(max_length=256, blank=False, null=False)
        numero = models.CharField(max_length=8, blank=True, null=True)
        bairro = models.CharField(max_length=256, blank=False, null=False)
        cidade = models.CharField(max_length=256, blank=False, null=False)
        estado = models.CharField(max_length=256, blank=False, null=False)
        cep = models.CharField(max_length=8, blank=False, null=False)
        pessoa = models.ForeignKey(Pessoa, blank=False, null=False, on_delete=models.CASCADE, related_name='veiculos')
        
        def __str__(self):
           return self.placa + "de" + self.pessoa
       
        class RegistroAcesso(models.Model):
           STATUS_CHOICES = (('E', 'Em andamento'),('F', 'Finalizado'),)
           
           pessoa = models.ForeignKey(Pessoa, blank=False, null=False, on_delete=models.CASCADE)
           veiculo = models.ForeignKey(Veiculo, blank=True, null=True, on_delete=models.CASCADE)
           data_hora_entrada = models.DateTimeField(blank=False, null=False)
           data_hora_saida = models.DateTimeField(blank=True, null=True)
           status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='E', blank=False, null=False)
           
           