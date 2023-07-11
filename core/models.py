from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.nome
    