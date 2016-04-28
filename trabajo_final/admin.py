from django.contrib import admin
from trabajo_final.models import beneficiario

# Register your models here.

@admin.register(beneficiario)
class beneficiarioAdmin(admin.ModelAdmin):

   list_display = ('nombres','apellido','documento','direccion')
   search_fields =  ('nombres','apellido','documento')

