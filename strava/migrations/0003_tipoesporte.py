# Generated by Django 5.1.2 on 2025-03-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strava', '0002_tipoequipamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEsporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esporte', models.CharField(choices=[('100m', '100 metros'), ('400m', '400 metros'), ('1km', '1 Quilômetro'), ('5km', '5 Quilômetros'), ('10km', '10 Quilômetros'), ('15km', '15 Quilômetros'), ('20km', '20 Quilômetros'), ('Meia Maratona', 'Meia maratona'), ('30km', '30 Quilômetros'), ('Maratona', 'Maratona'), ('Maior distância', 'Maior Distância'), ('Maior duração', 'Maior Duração')], default='100m', help_text='Selecione o esporte.', max_length=30, verbose_name='Esporte.')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
