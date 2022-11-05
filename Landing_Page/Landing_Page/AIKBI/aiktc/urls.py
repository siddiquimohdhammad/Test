from django.urls import path

from . import views

urlpatterns = [
    path('',views.home , name='index'),
    path('knowmore/',views.knowmore , name='knowmore'),
    path('registration/',views.registration, name='registration')
]