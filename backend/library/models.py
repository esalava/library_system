import datetime

from django.db import models, transaction


class User(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)

    @classmethod
    def get_id_by_username(cls, username):
        return User.objects.get(username=username)

    @classmethod
    def existe_usuario(cls, username):
        if User.objects.filter(username=username):
            return True
        return False

    @classmethod
    def create_usuario(cls, username):
        usuario_nuevo = User(username=username)
        usuario_nuevo.save()


class Libro(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=False)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=256)
    cantidad_disponible = models.PositiveIntegerField(default=0)

    @classmethod
    def create_libro(self, codigo, titulo, autor, cantidad):
        libro = Libro(codigo=codigo, titulo=titulo, autor=autor, cantidad_disponible=cantidad)
        libro.save()

    @classmethod
    def libros_por_coincidencia(cls, coincidencia: str):
        pass

    def devolver_libro_a_inventario(self, cantidad: int = 1):
        self.cantidad_disponible += cantidad
        self.save()

    @classmethod
    def get_libro_by_id(cls, id: int):
        libro = Libro.objects.get(pk=id)
        return libro

    @classmethod
    def get_catalogo(cls):
        #solo se deben mostrar los libros que tengan mas de 1 cantidad disponible
        return list(Libro.objects.filter(cantidad_disponible__gte=1).values())

    @classmethod
    def get_libros_por_ids(cls, ids: list):
        libros = Libro.objects.filter(id__in=ids)
        return list(libros.values('id', 'codigo', 'titulo', 'autor'))

    def disminuir_cantidad_disponible(self, cantidad=1):
        try:
            with transaction.atomic():
                if int(self.cantidad_disponible) > 0:
                    self.cantidad_disponible -= cantidad
                    self.save()
                    return True
                else:
                    return False
        except Exception as e:
            return False


    @classmethod
    def existe_libro(cls, id):
        if Libro.objects.filter(id=id).exists():
            return True
        return False


class Prestamo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    libro = models.ForeignKey(Libro, on_delete=models.DO_NOTHING)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField()
    fecha_devolucion = models.DateTimeField(null=True)

    @classmethod
    def solicitar_prestamo(
            cls,
            usuario: User,
            libro: Libro,
            fecha_fin: datetime
    ):
        prestamo = Prestamo(usuario=usuario, libro=libro, fecha_fin=fecha_fin)
        prestamo.save()

    def terminar_prestamo(self, libro):
        try:
            with transaction.atomic():
                libro.devolver_libro_a_inventario()
                self.fecha_devolucion = datetime.datetime.today()
                self.save()
        except Exception as e:
            return False

    @classmethod
    def tiene_prestamo_registrado(self, username, libro_id):
        username = User.get_id_by_username(username)
        res = Prestamo.objects.filter(
            usuario_id=username.id,
            libro_id=libro_id,
            fecha_devolucion=None
        ).exists()
        return res

    @classmethod
    def prestamos_actuales(
            cls,
    ):
        prestamos = Prestamo.objects.select_related('libro', 'usuario')\
            .filter(fecha_devolucion=None)
        prestamos = list(prestamos.values(
            'usuario__username',

            'id',
            'fecha_inicio',
            'fecha_fin',
            'libro__id',

            'libro__titulo',
            'libro__autor',
            'libro__titulo'
        ))
        return prestamos

    @classmethod
    def prestamos_actuales_por_usuario(
            cls,
            username
    ):
        #Los prestamos actuales son las que no tienen fecha de entrega
        usuario = User.get_id_by_username(username)
        prestamos = Prestamo.objects.select_related('libro', 'usuario')\
            .filter(
            usuario_id=usuario.id,
            fecha_devolucion=None
        )

        prestamos = list(prestamos.values(
            'usuario__username',

            'id',
            'fecha_inicio',
            'fecha_fin',
            'libro__id',

            'libro__titulo',
            'libro__autor',
            'libro__titulo',
            'libro__codigo',
        ))
        return prestamos

    @classmethod
    def get_prestamo_by_id(cls, id):
        return Prestamo.objects.get(pk=id)