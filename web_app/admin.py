from django.contrib import admin
from .models import WeedingPage, AssistanceForm, PreBodaForm, WishForm, Imagenes

# Register your models here.


class WeddingPageAdmin(admin.ModelAdmin):
    list_display = ['id',]


admin.site.register(WeedingPage, WeddingPageAdmin)


class AssistanceFormAdmin(admin.ModelAdmin):
    list_display = ['id','assistance', 'guests', 'companions', 'bus', 'about_food', 'sugerencia']


admin.site.register(AssistanceForm, AssistanceFormAdmin)


class PreBodaFormAdmin(admin.ModelAdmin):
    list_display = ['id','assistance', 'guests','companions', 'mood']


admin.site.register(PreBodaForm, PreBodaFormAdmin)


class WishFormdmin(admin.ModelAdmin):
    list_display = ['id', 'guests', 'wish']


admin.site.register(WishForm, WishFormdmin)


class ImagenesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]


admin.site.register(Imagenes, ImagenesAdmin)