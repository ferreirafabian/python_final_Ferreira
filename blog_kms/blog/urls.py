from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_post, name='crear_post'),
    path('eliminar/<int:pk>/', views.eliminar_post, name='eliminar_post'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('buscar/', views.buscar_fecha, name='buscar_fecha'),
    path('acerca/', views.acerca_de_mi, name='acerca_de_mi'),  # ← nueva ruta
]
