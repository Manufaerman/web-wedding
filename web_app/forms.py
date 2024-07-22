from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AssistanceForm, PreBodaForm, WishForm


class Assistance_Form(ModelForm):
    class Meta:
        model = AssistanceForm
        fields = {'assistance', 'guests','companions', 'bus', 'about_food', 'sugerencia'}
        field_classes = {
            'assistance': CheckboxSelectMultiple,
            'bus': CheckboxSelectMultiple,
            'about_food': CheckboxSelectMultiple}
        widgets = {
            'sugerencia': Textarea(attrs={'placeholder':'Puedes dejarnos un mensaje (i.e.alergia/intolerancia no contemplada en el campo anterior, alguna necesidad especial, etc).'}),

        }
        labels = {
            'assistance': 'Confirmación de asistencia - ¿vas a asistir a la boda?',
            'guests': 'Asistentes - Indica tu nombre y el de tu acompañante.',
            'companions': 'Indica solo el número de acompañantes',
            'bus': 'Desplazamiento - ¿Vas a utilizar servicio de autobús?',
            'about_food': 'Restricción alimentaria - ¿Tienes alguna alergia/intolerancia que debamos saber?'
        }


class PreBoda_Form(ModelForm):
    class Meta:
        model = PreBodaForm
        fields = {'assistance', 'guests', 'companions', 'mood'}
        field_classes = {
            'assistance': CheckboxSelectMultiple,
            'mood': CheckboxSelectMultiple,
        }
        labels = {
            'assistance': 'Confirmación de asistencia - ¿vas a asistir a la Preboda?',
            'guests': 'Asistentes - Indica tu nombre y el de tu acompañante',
            'companions': 'Indica SOLO !!! el número de acompañantes.',
        }


class Wish_Form(ModelForm):
    class Meta:
        model = WishForm
        fields = {'guests', 'wish'}
        widgets = {
            'wish': forms.Textarea(attrs={'rows': 3}),
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

