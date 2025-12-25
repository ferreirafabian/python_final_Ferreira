from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/password_change.html',
            success_url='/'  # redirige al inicio después de cambiar la contraseña
        ),
        name='password_change'
    ),
]
