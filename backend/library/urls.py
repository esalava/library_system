from django.urls import path
from . import views

urlpatterns = [
    path("catalogo", views.get_catalogo, name="catalogo"),
    path("admin/", views.admin, name="admin"),
    path("admin/registrar/", views.registrar_libro, name="registrar_libro"), #Aqui se registra un nuevo libro
    path("user/<str:username>", views.user, name="user"),
    path("user/<str:username>/prestar", views.prestar_libro, name="prestar_libro"), #Aqui se prestan libros
    path("user/<str:username>/devolver", views.devolver_libro, name="devolver_libro") #Aqui se prestan libros
]