from django.contrib import admin
from strava.models import TipoMarca
from strava.models import TipoEquipamento
from strava.models import TipoEsporte
from strava.models import TipoGenero

# Register your models here.

admin.site.register(TipoMarca)
admin.site.register(TipoEquipamento)
admin.site.register(TipoEsporte)
admin.site.register(TipoGenero)
