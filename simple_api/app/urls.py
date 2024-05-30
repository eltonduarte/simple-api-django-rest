from django.urls import path

# Import das minhas views
from app.views import listar_inserir_usuarios, atualizar_deletar_usuarios

urlpatterns = [
    path('', listar_inserir_usuarios),
    path('<int:pk>/', atualizar_deletar_usuarios),
]
