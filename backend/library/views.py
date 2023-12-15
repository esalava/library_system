import datetime
from django.http import JsonResponse, HttpResponseBadRequest
from .models import User, Libro, Prestamo
from django.views.decorators.csrf import csrf_exempt
from utils.dates import get_date_from_string, sobrepasa_fecha_maxima_entrega
import json


def user(request, username):
    if not User.existe_usuario(username):
        User.create_usuario(username)
    libros_prestados = Prestamo.prestamos_actuales_por_usuario(username)
    res = {"data": libros_prestados}
    return JsonResponse(res)


def get_catalogo(request):
    catalogo = Libro.get_catalogo()
    return JsonResponse({"data": catalogo})

@csrf_exempt
def prestar_libro(request, username):
    if request.method == 'POST':
        body = json.loads(request.body)
        libro_id = body.get('libro_id')
        fecha_fin = body.get('fecha_fin')
        dt_fecha_fin = get_date_from_string(fecha_fin)
        dt_fecha_prestamo = datetime.datetime.today()

        if not Libro.existe_libro(libro_id):
            return HttpResponseBadRequest("El libro no existe")

        if sobrepasa_fecha_maxima_entrega(dt_fecha_prestamo, dt_fecha_fin):
            return HttpResponseBadRequest("Sobrepasa fecha de entrega")

        if dt_fecha_fin <= dt_fecha_prestamo:
            return HttpResponseBadRequest("La fecha fin es menor a la fecha que esta realizando el prestamo")

        libro = Libro.get_libro_by_id(libro_id)

        if Prestamo.tiene_prestamo_registrado(username, libro.id):
            return HttpResponseBadRequest("Ya tiene prestado esta unidad")

        if not libro.disminuir_cantidad_disponible():
            return HttpResponseBadRequest("No existen unidades disponibles")

        usuario = User.get_id_by_username(username)
        Prestamo.solicitar_prestamo(usuario, libro, fecha_fin)

        return JsonResponse({"data": "Se ha prestado el libro correctamente"})


@csrf_exempt
def devolver_libro(request, username):
    if request.method == 'POST':
        prestamo_id = request.GET.get('prestamo_id')

        prestamo = Prestamo.get_prestamo_by_id(prestamo_id)

        if prestamo.fecha_devolucion:
            return HttpResponseBadRequest("Este prestamo ya ha sido terminado")

        libro = Libro.get_libro_by_id(prestamo.libro_id)
        prestamo.terminar_prestamo(libro)

        return JsonResponse({"data": "Se ha devuelto el libro correctamente"})
    return HttpResponseBadRequest("Hecho por Eduardo Salavarria :)")


def admin(request):
    libros_prestados = Prestamo.prestamos_actuales()
    return JsonResponse({'data': libros_prestados})


@csrf_exempt
def registrar_libro(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)

            titulo = body.get('titulo')
            autor = body.get('autor')
            cantidad_disponible = body.get('cantidad_disponible')
            codigo = body.get('codigo')

            if not (titulo and autor and cantidad_disponible and codigo):
                return HttpResponseBadRequest("No se puede registrar ese libro")

            Libro.create_libro(titulo=titulo, autor=autor, cantidad=cantidad_disponible, codigo=codigo)
            return JsonResponse({"data": "Se ha registrado el libro correctamente"})
        except Exception as e:
            return HttpResponseBadRequest("No se pudo registrar el libro")
    else:
        return HttpResponseBadRequest("Hecho por Eduardo Salavarria :)")
