from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('<slug:slug>/', detallesPost, name='detalle_post'),    
    path('generales/', generales, name='generales'),
    path('programacion/', programacion, name='programacion'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('videojuegos/', videojuegos, name='videojuegos'),
    path('tutoriales/', tutoriales, name='tutoriales'),
    
    
]