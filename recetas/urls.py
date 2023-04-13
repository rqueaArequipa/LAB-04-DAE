from django.urls import path
from . import views

app_name = 'receta'

urlpatterns = [
    path('',views.Index, name='index'),
    path('receta/', views.Recetas, name='receta'),
    path('preparacion/<int:autor_id>/<int:receta_id>/', views.Preparacion, name='preparacion'),
    path('register', views.Register, name='register'),
]