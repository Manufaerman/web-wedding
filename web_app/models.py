from django.db import models


class WeedingPage(models.Model):
    video = models.FileField(upload_to='videos')


class AssistanceForm(models.Model):
    ASSISTANCE_CHOICES = [('1', 'Si asistiré/asistiremos'), ('2', 'No, lamentableente no puedo asistir')]
    BUS_CHOICES = [('1', 'Si, necesitamos transporte'), ('2', 'No, usaremos el propio'), ('3', 'Si, solo ida'),
                   ('4', 'Si, solo vuelta')]
    FOOD_CHOICES = [('1', 'Si, intolerancia al gluten'), ('2', 'Si, soy vegano'), ('3', 'si, soy vevetariano'),
                    ('4', 'Otro, indicanoslo en el siguiente campo'), ('5', 'No, ninguna')]

    assistance = models.CharField(choices=ASSISTANCE_CHOICES, max_length=500)
    guests = models.CharField(max_length=200)
    companions = models.IntegerField(null=True, default=0)
    bus = models.CharField(choices=BUS_CHOICES, max_length=500)
    about_food = models.CharField(choices=FOOD_CHOICES, max_length=500)
    sugerencia = models.CharField(max_length=200, blank=True,)


class PreBodaForm(models.Model):
    ASSISTANCE_CHOICES = [('1', 'Si asistiré/asistiremos'), ('2', 'No, lamentableente no puedo asistir')]
    MOOD_CHOICES = [('1', 'la noche esta en pañales baby'), ('2', 'la última y nos vamos'), ('3', 'da igual, aqui nadie nos conoce'),
                    ('4', 'Si la vida te da limones, pide sal y tequila'),
                    ('5', 'Es que mi abuela fuma y ...'),
                    ('6', 'Un bidon de gasolina por favor !')]
    assistance = models.CharField(choices=ASSISTANCE_CHOICES, max_length=500)
    guests = models.CharField(max_length=200)
    companions = models.IntegerField()
    mood = models.CharField(max_length=500, choices=MOOD_CHOICES)


class WishForm(models.Model):
    guests = models.CharField(max_length=200)
    wish = models.CharField(max_length=500)

class Imagenes(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField()