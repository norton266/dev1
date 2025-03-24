# Generated by Django 5.1.2 on 2025-03-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMarca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('100m', '100 metros'), ('400m', '400 metros'), ('1km', '1 Quilômetro'), ('5km', '5 Quilômetros'), ('10km', '10 Quilômetros'), ('15km', '15 Quilômetros'), ('20km', '20 Quilômetros'), ('Meia Maratona', 'Meia maratona'), ('30km', '30 Quilômetros'), ('Maratona', 'Maratona'), ('Maior distância', 'Maior Distância'), ('Maior duração', 'Maior Duração')], default='100m', help_text='Selecione a marca.', max_length=20, verbose_name='Marca.')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
