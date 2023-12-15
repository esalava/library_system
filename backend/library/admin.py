from django.contrib import admin

# Register your models here.
from .models import User, Libro, Prestamo

admin.site.register(User)
admin.site.register(Libro)
admin.site.register(Prestamo)
