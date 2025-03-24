from django.utils.translation import gettext_lazy as _
from django.db import models

class StatusTipoMarca(models.TextChoices):
    CEM = '100m', _('100 metros')
    QUATROCENTOS = '400m', _('400 metros')
    UMKM = '1km', _('1 Quilômetro')
    CINCOKM = '5km', _('5 Quilômetros')
    DEZKM = '10km', _('10 Quilômetros')
    QUINZEKM = '15km', _('15 Quilômetros')
    VINTEKM = '20km', _('20 Quilômetros')
    MEIA = 'Meia Maratona', _('Meia maratona')
    TRINTAKM = '30km', _('30 Quilômetros')
    MARATONA = 'Maratona', _('Maratona')
    LONGA_DISTANCIA = 'Maior distância', _('Maior Distância')
    LONGA_DURACAO = 'Maior duração', _('Maior Duração')


class StatusTipoEquipamento(models.TextChoices):
    SNEAKER = 'Tênis', _('Tênis')
    BIKE = 'Bicicleta', _('Bicicleta')
    SMART_DEVICE = 'Dispositivo Inteligente', _('Dispositivo Inteligente')

class StatusTipoEsporte(models.TextChoices):
    RUN = 'Corrida', _('Corrida')
    TRAIL_RUN = 'Corrida de trilhas', _('Corrida de trilhas')
    BIKE = 'Treino de bicicleta', _('Treino de bicicleta')
    WALK = 'Caminhada', _('Caminhada')
    HIIT = 'Treino de alta intensidade', _('Treino de alta intensidade')
    STRENGTH = 'Treino de força', _('Treino de força')
    CARDIO = 'Treino aeróbico', _('Treino aeróbico')
    SWIMMING = 'Natação', _('Natação')

class StatusTipoGenero(models.TextChoices):
    MAN = 'Homem', _('Homem')
    WOMAN = 'Mulher', _('Mulher')
    NON_BINARY = 'Não binário', _('Não binário')
    NOT_INFORMED = 'Não informado', _('Não informado')