from django.core.validators import MinValueValidator,MaxValueValidator
from .base_model import BaseModel
from django.db import models
from my_app.enumerations import Status

class Example(BaseModel):
    description = models.CharField(
        max_length=100, null=False, blank=False,
        help_text='Descrição para um exemplo',
        verbose_name='Descrição',
    )

    quality = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(0)],
        default=50,
        help_text='Valor numérico para a qualidade do exemplo. Entre 0 e 100',
        verbose_name='Qualidade',
    )

    balance = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,

    )