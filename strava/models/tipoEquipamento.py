from .base_model import BaseModel
from django.db import models
from strava.enumerations import StatusTipoEquipamento

class TipoEquipamento(BaseModel):
    equipamento = models.CharField(
        max_length=30,
        null = False, blank = False,
        choices=StatusTipoEquipamento, default=StatusTipoEquipamento.SNEAKER,
        help_text='Selecione o equipamento.',
        verbose_name='Equipamento.'
    )

def __str__ (self):
    return f"{self.equipamento}"

class Meta:
    verbose_name = "Equipamento"
    verbose_name_plural = "Equipamentos"