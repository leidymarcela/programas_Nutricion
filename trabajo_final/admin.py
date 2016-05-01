from django.contrib import admin
from trabajo_final.models import beneficiario

# Register your models here.

@admin.register(beneficiario)
class beneficiarioAdmin(admin.ModelAdmin):

   list_display = ('name','apellido','documento','numero_documento','direccion','barrio','genero','fecha_de_nacimiento','eps')
   search_fields =  ('name','apellido','documento')

