from django.db import models

# Create your models here.
class ContactoMensaje(models.Model):
    nombre = models.CharField(verbose_name='Nombre',max_length=15)
    apellidoPaterno = models.CharField(verbose_name='Apellido Paterno',max_length=32)
    apellidoMaterno = models.CharField(verbose_name='Apellido Materno',max_length=32)
    correo = models.CharField(verbose_name='Correo Electronico',max_length=32)
    comentarios = models.CharField(verbose_name='Comentarios',max_length=100)
    creacion = models.DateTimeField(verbose_name='Fecha Mensaje', auto_now_add=True)

class Marca(models.Model):
    nombreMarca = models.CharField(verbose_name='Nombre Marca',max_length=32)
    creacion = models.DateTimeField(verbose_name='Creacion Marca', auto_now_add=True)

    def __str__(self):
        return self.nombreMarca

class Categoria(models.Model):
    nombreCategoria = models.CharField(verbose_name='Nombre Categoria',max_length=32)
    creacion = models.DateTimeField(verbose_name='Creacion Categoria', auto_now_add=True)

    def __str__(self):
        return self.nombreCategoria

class Zapatilla(models.Model):
    nombre = models.CharField(verbose_name='Nombre Zapatilla',max_length=32)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.IntegerField(verbose_name='Precio')
    encabezado = models.CharField(verbose_name='Encabezado',max_length=100)
    descripcion = models.CharField(verbose_name='Descripcion',max_length=300)
    info1 = models.CharField(verbose_name='Info1',max_length=300,null=True,blank=True)
    info2 = models.CharField(verbose_name='Info2',max_length=300,null=True,blank=True)
    info3 = models.CharField(verbose_name='Info3',max_length=300,null=True,blank=True)
    imagen = models.ImageField(verbose_name='Imagen',upload_to='zapatillas',null=True,blank=True)
    creacion = models.DateTimeField(verbose_name='Creacion Zapatilla', auto_now_add=True)
