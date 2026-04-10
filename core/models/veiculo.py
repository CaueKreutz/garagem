from django.db import models

from core.models import Acessorio, Cor, Modelo


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        default=0
    )
    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.PROTECT,
        related_name='veiculos'
    )
    cor = models.ForeignKey(
        Cor,
        on_delete=models.PROTECT,
        related_name='veiculos'
    )
    acessorios = models.ManyToManyField(
        Acessorio,
        related_name='veiculos',
        blank=True
    )

    def __str__(self):
        return f"{self.id} - {self.modelo} - {self.cor} - {self.ano}"

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"