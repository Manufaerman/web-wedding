# Generated by Django 5.0.6 on 2024-07-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_assistanceform_companions_prebodaform_companions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prebodaform',
            name='mood',
            field=models.CharField(choices=[('1', 'la noche esta en pañales baby'), ('2', 'la ùltima y nos vamos'), ('3', 'da igual, aqui nadie nos conoce'), ('4', 'Si la vida te da limones, pide sal y tequila'), ('5', 'Es que mi abuela fuma y ...'), ('6', 'Un bidon de gasolina por favor !')], max_length=500),
        ),
    ]
