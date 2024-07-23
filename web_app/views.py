from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .models import WeedingPage
from django.db.models import Sum
from datetime import datetime, timedelta
from .forms import Assistance_Form, PreBoda_Form
from .models import AssistanceForm, PreBodaForm, WishForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, Wish_Form

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    guests = AssistanceForm.objects.all()
    pre_boda = PreBodaForm.objects.all()

    number_companions_preboda = PreBodaForm.objects.values('companions').aggregate(Sum('companions'))
    number_companions_boda = AssistanceForm.objects.values('companions').aggregate(Sum('companions'))
    number_passengers_bus = AssistanceForm.objects.filter(bus='1',)

    passengers = 0
    for passenger in number_passengers_bus:
        passengers += 1
        if passenger.companions:
            passengers += passenger.companions




    if number_companions_boda['companions__sum'] is None:
        number_of_guests_preboda = number_companions_preboda['companions__sum'] + len(pre_boda)
        number_of_guests_boda = len(guests)
        return render(request, 'dashboard.html',
                              {'guests': guests, 'pre_boda': pre_boda, 'number_of_guests_preboda': number_of_guests_preboda,
                               'number_of_guests_boda': number_of_guests_boda, 'passengers':passengers})

    elif number_companions_preboda['companions__sum'] is None:
        number_of_guests_boda = number_companions_boda['companions__sum'] + len(guests)
        number_of_guests_preboda = len(pre_boda)
        return render(request, 'dashboard.html',
                              {'guests': guests, 'pre_boda': pre_boda, 'number_of_guests_preboda': number_of_guests_preboda,
                               'number_of_guests_boda': number_of_guests_boda, 'passengers':passengers})

    number_of_guests_preboda = number_companions_preboda['companions__sum'] + len(pre_boda)
    number_of_guests_boda = number_companions_boda['companions__sum'] + len(guests)
    return render(request, 'dashboard.html',
                      {'guests': guests, 'pre_boda': pre_boda, 'number_of_guests_preboda': number_of_guests_preboda,
                       'number_of_guests_boda': number_of_guests_boda, 'passengers':passengers})





def alojamiento(request):
    return render(request, 'alojamiento.html')

def regalo_boda(request):
    return render(request, 'regalo.html')

def autobuses(request):
    return render(request, 'autobuses.html')

def home(request, **kwargs):
    form = PreBoda_Form()
    formdos = Assistance_Form()
    formtres = Wish_Form()
    today = datetime.now()
    wishes = WishForm.objects.all()
    wedding_date_ = '20241012 12:00:00'
    wedding_date = datetime.strptime(wedding_date_, '%Y%m%d %H:%M:%S')
    time_to_wedding = wedding_date - today
    if request.method == 'GET':
        return render(request, 'home.html', {
                                             'time_to_wedding': time_to_wedding,
                                             'form': form, 'formdos': formdos,
                                             'formtres': formtres,
                                             'wishes': wishes,
                                                                            })

    if request.method == 'POST':

        if 'mood' in request.POST:
            post = 'post'
            form = PreBoda_Form(request.POST)
            formdos = Assistance_Form(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()

                return render(request, 'home.html', {'time_to_wedding': time_to_wedding, 'post': post, 'formdos': formdos, 'form': form, 'formtres': formtres,})
            else:
                return HttpResponse('the first form is not valid')


        else:
            formtres = Wish_Form(request.POST)
            if formtres.is_valid():
                instance = formtres.save(commit=False)
                instance.save()
                ancla = 'ancla'
                return render(request, 'home.html', {'time_to_wedding': time_to_wedding, 'form': form, 'formdos':formdos, 'formtres': formtres, 'ancla': ancla})


def second_form_view(request):
    today = datetime.now()
    wedding_date_ = '20241012 12:00:00'
    wedding_date = datetime.strptime(wedding_date_, '%Y%m%d %H:%M:%S')
    time_to_wedding = wedding_date - today
    formdos = Assistance_Form()
    formtres = Wish_Form()
    if 'sugerencia' in request.POST:
        form = PreBoda_Form()
        ancla = 'ancla'
        postdos = 'postdos'
        formdos = Assistance_Form(request.POST)
        if formdos.is_valid():
            instance = formdos.save(commit=False)
            instance.save()

            return render(request, 'home.html', {'time_to_wedding': time_to_wedding,
                                                 'postdos': postdos,
                                                 'form': form,
                                                 'formdos':formdos,
                                                 'formtres': formtres,
                                                 'ancla': ancla,
                                              })
        else:
            return HttpResponse('the second form is not valid')

