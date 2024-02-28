from django.contrib import admin
from django.urls import path
from.views import*



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello1/',hello1,name='hello'),
    path('', newHomePage, name='newHomePage'),
    path('travelPackage/',travelPackage,name='travelPackage'),

    path('print1/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),

    path('r/',randomcall,name='randomcall'),
    path('randomLogic/',randomlogic,name='randomlogic'),

    path('getdate1/', getdate1, name='getdate1'),
    path('get_date/', get_date, name='get_date'),

    path('registercalling/', registercalling, name='registercalling'),
    path('registerloginfunction/', registerloginfunction, name='registerloginfunction'),

    path('piechartcalling/', piechartcalling, name='piechartcalling'),
    path('pie_chart/', pie_chart, name='pie_chart'),

    path('carcalling/', carcalling, name='carcalling'),

    path('weatherpagecall/', weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),

    path('feedbackcalling/', feedbackcalling, name='feedbackcalling'),
    path('feedbackfunction/', feedbackfunction, name='feedbackfunction'),

    path('login/',login,name='login'),
    path('login1/', login1, name='login1'),

    path('signup/',signup,name='signup'),
    path('signup1/', signup1, name='signup1'),

    path('logout/',logout,name='logout'),



]
