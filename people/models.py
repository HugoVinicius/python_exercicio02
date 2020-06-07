from django.db import models

class Cargo(models.Model):
    nome = models.CharField(max_length=200)
    salario = models.FloatField(default=845, null=True)

class Estado(models.Model):
    nome = models.CharField(max_length=200)
    prefeito = models.CharField(max_length=50)
    codigo_ibge = models.CharField(max_length=15)

class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	idade = models.IntegerField(default=0)
	data_nascimento = models.DateField(null=True)
	cpf = models.CharField(max_length=14, null=True)
	cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True)

class Endereco(models.Model):
	pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
	logradouro = models.CharField(max_length=200)
	numero = models.IntegerField(default=0)
	bairro = models.CharField(max_length=100,null=True)
	cep = models.CharField(max_length=9)



