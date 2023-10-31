from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=False)
    email = models.EmailField(max_length=255)
    senha = models.CharField(max_length=255, default='')

class Filme(models.Model):
    filme_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    sinopse = models.TextField()
    ano_lancamento = models.PositiveIntegerField()
    classificacao_indicativa = models.CharField(max_length=10)
    diretor = models.ForeignKey('Diretor', on_delete=models.CASCADE)
    idioma = models.CharField(max_length=50)
    pontuacao_media = models.DecimalField(max_digits=3, decimal_places=2)
    url_imagem_capa = models.URLField(max_length=255)
    url_trailer = models.URLField(max_length=255)

class Ator(models.Model):
    ator_id = models.AutoField(primary_key=True)
    nome_ator = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)

class Diretor(models.Model):
    diretor_id = models.AutoField(primary_key=True)
    nome_diretor = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)

class CategoriaFilme(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=50)

class Elenco(models.Model):
    filme = models.ForeignKey('Filme', on_delete=models.CASCADE)
    ator = models.ForeignKey('Ator', on_delete=models.CASCADE)

class DiretorFilme(models.Model):
    filme = models.ForeignKey('Filme', on_delete=models.CASCADE)
    diretor = models.ForeignKey('Diretor', on_delete=models.CASCADE)

class FilmeCategoria(models.Model):
    filme = models.ForeignKey('Filme', on_delete=models.CASCADE)
    categoria = models.ForeignKey('CategoriaFilme', on_delete=models.CASCADE)

# class AvaliacaoUsuario(models.Model):
    # avaliacao_id = models.AutoField(primary_key=True)
    # filme = models.ForeignKey('Filme', on_delete=models.CASCADE)
    # usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)  # Adicione essa tabela se necessário
    # classificacao = models.PositiveSmallIntegerField()
    # comentario = models.TextField()





