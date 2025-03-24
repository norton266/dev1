from .base_model import BaseModel
from django.db import models
from strava.enumerations import StatusTipoGenero

class TipoGenero(BaseModel):
    genero = models.CharField(
        max_length=30,
        null = False, blank = False,
        choices=StatusTipoGenero, default=StatusTipoGenero.NOT_INFORMED,
        help_text='Selecione o gênero.',
        verbose_name='Gênero.'
    )

    def __str__ (self):
        return f"{self.genero}"

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"