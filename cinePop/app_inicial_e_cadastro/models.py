from django.contrib.auth.models import User
from django.db import models
"""
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

    Fim do sqlite

    """
# class AvaliacaoUsuario(models.Model):
    # avaliacao_id = models.AutoField(primary_key=True)
    # filme = models.ForeignKey('Filme', on_delete=models.CASCADE)
    # usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)  # Adicione essa tabela se necessário
    # classificacao = models.PositiveSmallIntegerField()
    # comentario = models.TextField()

# Inicio do Mysql

class Categoria(models.Model):
    id_cat = models.IntegerField(primary_key=True)
    nome_cat = models.CharField(max_length=50, null=False)

class Nacionalidade(models.Model):
    id_nacionalidade = models.IntegerField(primary_key=True)
    nacionalidade = models.CharField(max_length=50, null=False)

class Diretor(models.Model):
    id_diretor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)
    data_nascimento = models.DateField(null=False)
    nacionalidade = models.ForeignKey(Nacionalidade, on_delete=models.CASCADE)

class Ator(models.Model):
    id_ator = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)
    data_nascimento = models.DateField(null=False)
    nacionalidade = models.ForeignKey(Nacionalidade, on_delete=models.CASCADE)

class Filme(models.Model):
    id_filme = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=False)
    sinopse = models.CharField(max_length=300, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ano_lancamento = models.DateField(null=False)
    class_indicativa = models.CharField(max_length=5, null=False)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    idioma = models.CharField(max_length=50, null=True)
    url_capa = models.CharField(max_length=100, null=True)
    url_trailer = models.CharField(max_length=100, null=True)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)
    senha = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=60, null=False)

class Avaliacao(models.Model):
    id_avaliacao = models.AutoField(primary_key=True)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    classificacao = models.CharField(max_length=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=False)
    comentario = models.CharField(max_length=200, null=True)




