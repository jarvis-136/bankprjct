from django.urls import path
from . import views

app_name = "bankapp"
urlpatterns = [
    path('', views.home, name='home'),
    path('ulogin/',views.ulogin,name='ulogin'),
    path('form/',views.form,name='form'),
    path('register/',views.register,name='register'),
    path('mpage/',views.mpage,name='mpage'),
    path('ulogout/',views.ulogout,name='ulogout'),

]
