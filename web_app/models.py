from django.db import models


class WeedingPage(models.Model):
    video = models.FileField(upload_to='videos')


class AssistanceForm(models.Model):
    ASSISTANCE_CHOICES = [('1', 'Si asistiré/asistiremos'), ('2', 'No, lamentableente no puedo asistir')]
    BUS_CHOICES = [('1', 'Si, ida y vuelta'), ('2', 'No, usaremos el propio'),
                   ('4', 'Si, solo vuelta')]
    FOOD_CHOICES = [('1', 'Si, intolerancia al gluten'), ('2', 'Si, soy vegano'), ('3', 'si, soy vegetariano'),
                    ('4', 'Otro, indicanoslo en el siguiente campo'), ('5', 'No, ninguna')]

    assistance = models.CharField(choices=ASSISTANCE_CHOICES, max_length=500, default='1')
    guests = models.CharField(max_length=200)
    companions = models.IntegerField(null=True, default=0)
    bus = models.CharField(choices=BUS_CHOICES, max_length=500, default='2')
    about_food = models.CharField(choices=FOOD_CHOICES, max_length=500, default='5')
    sugerencia = models.CharField(max_length=200, blank=True,)


class PreBodaForm(models.Model):
    ASSISTANCE_CHOICES = [('1', 'Si asistiré/asistiremos'), ('2', 'No, lamentablemente no puedo asistir')]
    MOOD_CHOICES = [('1', 'la noche esta en pañales baby'), ('2', 'la última y nos vamos'), ('3', 'da igual, aqui nadie nos conoce'),
                    ('4', 'Si la vida te da limones, pide sal y tequila'),
                    ('5', 'Es que mi abuela fuma y ...'),
                    ('6', 'Un bidon de gasolina por favor !')]

    assistance = models.CharField(choices=ASSISTANCE_CHOICES, max_length=500, default='1')
    guests = models.CharField(max_length=200)
    companions = models.IntegerField(default=0)
    mood = models.CharField(max_length=500, choices=MOOD_CHOICES, default='5')


class WishForm(models.Model):
    guests = models.CharField(max_length=200)
    wish = models.CharField(max_length=500)

class Imagenes(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField()