from django.db import models

# Create your models here.

class Pessoa(models.Model):
	nome=models.CharField('nome', max_length=50)
	email=models.CharField('email', max_length=70)

	def __str__(self):
		return self.nome

class PessoaJuridica(Pessoa):
	cnpj=models.CharField('cnpj', max_length=14)
	razaoSocial=models.CharField('razaoSocial', max_length=50)


class Autor(Pessoa):
	curriculo=models.TextField()
	artigos=models.TextField()


class PessoaFisica(Pessoa):
	cpf=models.CharField('cpf', max_length=11)


class Evento(models.Model):
	nome=models.CharField('nome', max_length=50)
	eventoPrincipal=models.CharField('eventoPrinciapal', max_length=50)
	sigla=models.CharField('sigla', max_length=3)
	dataEhoraDeInicio=models.DateTimeField(blank=True, null=True)
	palavrasChave=models.CharField('palavrasChave', max_length=50)
	logotipo=models.CharField('logotipo', max_length=50)
	
	realizador=models.ForeignKey(Pessoa,null=True,blank=False)
	
	cidade=models.CharField('cidade', max_length=50)
	uf=models.CharField('uf', max_length=2)
	endereco=models.TextField()
	cep=models.CharField('cep', max_length=8)

	def __str__(self):
		return "Evento: "+self.nome


class EventoCientifico(Evento):
	issn=models.CharField('issn', max_length=50)

	def __str__(self):
		return "ISSN: "+issn


class ArtigoCientifico(models.Model):
	titulo=models.CharField('titulo', max_length=50)
	evento=models.ForeignKey(EventoCientifico, null=True, blank=False)
	autores=models.ManyToManyField(Autor)
	
	def __str__(self):
		return "Título: "+titulo


#class AutoresArtigoCientifico(models.Model):
#	autores=models.ForeignKey(Autor, blank=True, null=True)
#	artigos=models.ForeignKey(ArtigoCientifico, blank=True, null=True)
#
#	def __str__(self):
#		return "Autor:"+self.autores.nome+" Artigo: "+self.artigos.titulo