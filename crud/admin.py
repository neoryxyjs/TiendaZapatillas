from django.contrib import admin
from .models import * 

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ('id','creacion')
    list_display = ('id','nombre','apellidoPaterno','apellidoMaterno','correo','creacion')
    ordering = ('nombre','apellidoPaterno')

class MarcaAdmin(admin.ModelAdmin):
    readonly_fields = ('id','creacion')
    list_display = ('id','nombreMarca','creacion')
    ordering = ('nombreMarca',)

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('id','creacion')
    list_display = ('id','nombreCategoria','creacion')
    ordering = ('nombreCategoria',)

class ZapatillaAdmin(admin.ModelAdmin):
    readonly_fields = ('id','creacion')
    list_display = ('id','nombre','marca','categoria','precio','creacion')
    ordering = ('nombre',)

admin.site.register(ContactoMensaje,ContactoAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Zapatilla,ZapatillaAdmin)