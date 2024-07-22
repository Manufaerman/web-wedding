# Generated by Django 5.0.6 on 2024-07-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssistanceForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistance', models.CharField(choices=[('1', 'Si asistiré/asistiremos'), ('2', 'No, lamentableente no puedo asistir')], max_length=500)),
                ('guests', models.CharField(max_length=200)),
                ('bus', models.CharField(choices=[('1', 'Si, necesitamos transporte'), ('2', 'No, usaremos el propio')], max_length=500)),
                ('about_food', models.CharField(choices=[('1', 'Si, intolerancia al gluten'), ('2', 'Si, soy vegano'), ('3', 'si, soy vevetariano'), ('4', 'Otro, indicanoslo en el siguiente campo')], max_length=500)),
                ('sugerencia', models.CharField(max_length=200)),
            ],
        ),
    ]