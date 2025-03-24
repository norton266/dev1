from .base_model import BaseModel
from django.db import models
from strava.enumerations import StatusTipoEsporte

class TipoEsporte(BaseModel):
    esporte = models.CharField(
        max_length=30,
        null = False, blank = False,
        choices=StatusTipoEsporte, default=StatusTipoEsporte.RUN,
        help_text='Selecione o esporte.',
        verbose_name='Esporte.'
    )

def __str__ (self):
    return f"{self.esporte}"

class Meta:
    verbose_name = "Esporte"
    verbose_name_plural = "Esportes"