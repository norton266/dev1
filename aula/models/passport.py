from django.db import models
from .person import Person

class Passport(models.Model):
    number = models.CharField(max_length=100, verbose_name='Número do passaporte')
    issue_date = models.DateField(verbose_name='Issue Date')
    expiration_date = models.DateField(verbose_name='Data de vencimento')
    owner = models.OneToOneField(Person,
                                 on_delete=models.CASCADE,
                                 primary_key=True)

    def __str__(self):
        return self.owner.name