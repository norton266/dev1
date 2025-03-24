from django.contrib import admin
from my_app.models import Tag
from my_app.models import Example

# Register your models here.

admin.site.register(Tag)
admin.site.register(Example)
