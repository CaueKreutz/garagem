from django.db import models


class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, null=True, blank=True)
    categoria = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        marca_texto = self.marca.upper() if self.marca else ''
        return f"{self.id} - {marca_texto} {self.nome.upper()}".strip()

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"