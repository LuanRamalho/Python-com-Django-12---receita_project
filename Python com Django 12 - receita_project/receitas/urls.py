from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_receitas, name='lista_receitas'),
    path('receita/<int:pk>/', views.detalhe_receita, name='detalhe_receita'),
]
