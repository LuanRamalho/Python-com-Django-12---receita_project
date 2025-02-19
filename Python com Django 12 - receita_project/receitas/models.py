from django.db import models

class Receita(models.Model):
    nome = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()  # tempo de preparo em minutos
    porcoes = models.IntegerField()
    categoria = models.CharField(max_length=100)
    imagem_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nome
