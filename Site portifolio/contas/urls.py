from django.urls import path
from . import views

app_name = "contas"

urlpatterns = [
    path('entrar/', views.entrar, name='entrar'),
    path("inscrever/", views.inscrever, name="inscrever"),
    path("esqueci-a-senha/", views.esqueciASenha, name="esqueci"),
    path("lembrar/", views.lembrar, name="lembrar"),
]
