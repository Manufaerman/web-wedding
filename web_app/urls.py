from django.urls import path
from .views import home, dashboard, regalo_boda, alojamiento, user_login, user_logout, user_signup, second_form_view,autobuses



urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('regalo/', regalo_boda, name='regalo'),
    path('autobuses/', autobuses, name='autobuses'),
    path('alojamiento/', alojamiento, name='alojamiento'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('second_form_view/', second_form_view, name='second_view_home')

]