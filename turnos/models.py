from django.db import models
from datetime import datetime

ESTADOS = (
	(0 , 'Nuevo'),   # locos con menos de 6 meses d antiguedad
    (1 , 'Activo'),  # paga al dia
    (2 , 'Pasivo'),  # no paga
    (3 , 'Baja'),    # se fue o lo dieron de baja por moroso hdp
)

# Create your models here.

class Prestadora(models.Model):
	nombre = models.CharField (max_length=100)
	telefono = models.IntegerField ()
	direccion = models.CharField (max_length=100)
	
	def __unicode__(self):
		return self.nombre

class Profesional(models.Model):
	nombre = models.CharField (max_length=100)
	apellido = models.CharField (max_length=100)
	documento = models.IntegerField ()
	matricula = models.IntegerField ()
	telefono = models.IntegerField ()
	direccion = models.CharField (max_length=100)
	localidad = models.CharField (max_length=100)
	provincia = models.CharField (max_length=100)
	
	class Meta:
		verbose_name_plural = ('Profesionales')
		
	def __unicode__(self):
		return (self.nombre + ' ' + self.apellido)


class Afiliado(models.Model):
	cod_afiliado = models.CharField (max_length=100)
	nombre = models.CharField (max_length=100)
	apellido = models.CharField (max_length=100)
	documento = models.IntegerField ()
	estado = models.IntegerField (choices=ESTADOS)
	prestadora = models.ForeignKey(Prestadora)
	telefono = models.IntegerField ()
	direccion = models.CharField (max_length=100)
	localidad = models.CharField (max_length=100)
	provincia = models.CharField (max_length=100)
	fecha_nacimiento = models.DateField ()
	fecha_alta = models.DateField (default = datetime.today())
		
	def __unicode__(self):
		return (self.nombre + ' ' + self.apellido)


class Prestacion(models.Model):
	codigo = models.IntegerField ()
	descripcion = models.CharField (max_length=100)

	class Meta:
		verbose_name_plural = ('Prestaciones')
		
	def __unicode__(self):
		return self.descripcion

class Prestacion_afiliado(models.Model):
	afiliado = models.ForeignKey(Afiliado)
	prestacion = models.ManyToManyField(Prestacion)
	profesional = models.ForeignKey(Profesional)
	tiempo = models.DateTimeField(default = datetime.now)

	class Meta:
		verbose_name = ('Prestacion por afiliado')
		verbose_name_plural = ('Prestaciones por afiliado')
		
	def __unicode__(self):
		return (str(self.tiempo) + ' - ' + self.afiliado.nombre + ' ' + self.afiliado.apellido)


class Turno(models.Model):
	tiempo = models.DateTimeField(default = datetime.now)
	afiliado = models.ForeignKey(Afiliado)
	profesional = models.ForeignKey(Profesional)
	
	def __unicode__(self):
		return (self.afiliado.name + ' ' + self.afiliado.apellido )
