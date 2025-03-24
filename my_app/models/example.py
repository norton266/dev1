from django.core.validators import MinValueValidator,MaxValueValidator
from .base_model import BaseModel
from django.db import models
from my_app.enumerations import Status

class Example(BaseModel):
    description = models.CharField(
        max_length=100, null=False, blank=False,
        help_text="Descrição para um exemplo.",
        verbose_name="Descrição",
    )
    quality = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=50,
        help_text="Valor número para a qualidade do exemplo. Entre 0 e 100.",
        verbose_name="Qualidade",
    )
    balance = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        max_digits=6, decimal_places=2, default=0.00,
        help_text="Saldo financeiro. Valores entre 0 e 1000.",
        verbose_name="Saldo",
    )
    percentage = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.00, null=True, blank=True,
        help_text="Um exemplo de Float. Entre o e 100. Diversas casas decimais.",
        verbose_name="Percentage",
    )
    email = models.EmailField(
        max_length=254, null=False, blank=False, unique=True,
        help_text="E-mail do exemplo.",
        verbose_name="E-mail",
    )
    url = models.URLField(
        max_length=254, null=False, blank=False,
        help_text="URL externa.",
        verbose_name="URL",
    )
    status = models.CharField(
        max_length=3, null=False, blank=False,
        choices=Status, default=Status.NEW,
        help_text="Selecione o status para o exemplo.",
        verbose_name="Status",
    )

    def __str__(self):
        return f"{self.description} ({self.status}-{self.get_status_display()})"  # campo do tipo charfield com choices, libera o metodo get_status_display. mOstra o que está nos parenteses, na classe Status

    class Meta:
        verbose_name = "Exemplo"
        verbose_name_plural = "Exemplos"
        ordering = ("status", "-description",)