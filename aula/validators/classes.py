from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible

@deconstructible

class CodValidator:

    def __init__(self, cod="0000000000"):
        self.code = cod

    def __call__(self, valor):
        if valor == self.code:
            raise ValidationError(
                _("Valor inválido"),
                params={"valor": valor},
                code="invalid"
            )

    def __eq__(self, other):
        return (
            isinstance(other, CodValidator)
            and self.code == other.code
        )