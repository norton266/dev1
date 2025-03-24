from .base_model import BaseModel
from django.db import models
from strava.enumerations import StatusTipoMarca

class TipoMarca(BaseModel):
    marca = models.CharField(
        max_length=20,
        null = False, blank = False,
        choices=StatusTipoMarca, default=StatusTipoMarca.CEM,
        help_text='Selecione a marca.',
        verbose_name='Marca.'
    )

    def __str__(self):
        return f"{self.get_status_display()}"

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"