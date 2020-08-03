from django.urls import path
from . import views
app_name = 'employer'

urlpatterns = [
    path('', views.list_of_companies, name='listofcompanies'),
    path('registration/', views.registration, name='registration'),
    path('registration/add_company',views.add_company, name='add_company'),
    path('previous/', views.previous,name="previous"),
    path('parkinginfo/', views.parkinginfo, name="parkinginfo"),
    path('roomreservation/',views.roomreservation,name="roomreservation")
]