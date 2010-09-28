from django.contrib import admin
from turnos.models import Afiliado, Turno, Profesional, Prestadora, Prestacion, Prestacion_afiliado

class AfiliadoAdmin(admin.ModelAdmin):
  list_display = ('cod_afiliado', 'nombre', 'apellido', 'documento', 'estado', 'prestadora', 'telefono', 'direccion', 'localidad', 'fecha_nacimiento', 'fecha_alta')

class ProfesionalAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'documento', 'matricula', 'telefono', 'direccion', 'localidad', 'provincia')

class TurnoAdmin(admin.ModelAdmin):
	list_display = ('tiempo', 'afiliado', 'profesional')

class Prestacion_afiliadoAdmin(admin.ModelAdmin):
	list_display = ('afiliado', 'profesional', 'tiempo')

class PrestacionAdmin(admin.ModelAdmin):
	list_display = ( 'codigo', 'descripcion')

class PrestadoraAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'telefono', 'direccion')

admin.site.register(Afiliado, AfiliadoAdmin)
admin.site.register(Turno, TurnoAdmin)
admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Prestadora, PrestadoraAdmin)
admin.site.register(Prestacion, PrestacionAdmin)
admin.site.register(Prestacion_afiliado, Prestacion_afiliadoAdmin)
