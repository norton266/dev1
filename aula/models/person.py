from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome completo')
    birth_date = models.DateField(verbose_name='Data de nascimento')
    cpf = models.CharField(max_length=100, verbose_name='CPF')

    def __str__(self):
        return self.name