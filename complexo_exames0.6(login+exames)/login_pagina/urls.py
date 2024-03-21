from django.urls import path
from . import views

app_name='login_cliente'

urlpatterns = [
    path('', views.cliente_login, name='cliente_login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('adicionar-exames/', views.registro_exames, name='registro_exames'),
    path('exames/', views.ver_exames, name='ver_exames'),
]