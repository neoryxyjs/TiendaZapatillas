from django import forms
from django.forms import ModelForm
from .models import *

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombreCategoria'
        ]
        labels = {
            'nombreCategoria':'Nombre de la Categoria'
        }
        widgets = {
            'nombreCategoria':forms.TextInput(attrs={'class':'form-control','id':'nombreCategoria','name':'nombreCategoria','onblur':'validarNombreCategoria()'})
        }

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = [
            'nombreMarca'
        ]
        labels = {
            'nombreMarca':'Nombre de la Marca'
        }
        widgets = {
            'nombreMarca':forms.TextInput(attrs={'class':'form-control','id':'nombreMarca','name':'nombreMarca','onblur':'validarNombreMarca()'})
        }

class ZapatillaForm(ModelForm):
    class Meta:
        model = Zapatilla
        fields = [
            'nombre',
            'marca',
            'categoria',
            'precio',
            'encabezado',
            'descripcion',
            'imagen',
            'info1',
            'info2',
            'info3'
        ]
        labels = {
            'nombre':'Nombre de la Zapatilla',
            'marca':'Marca',
            'categoria':'Categoria',
            'precio':'Precio',
            'encabezado':'Encabezado',
            'descripcion':'Descripcion',
            'imagen':'Imagen',
            'info1':'Informacion 1',
            'info2':'Informacion 2',
            'info3':'Informacion 3'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','id':'nombre','name':'nombre','onblur':'validarNombre()'}),
            'marca':forms.Select(attrs={'class':'form-control','id':'marca','name':'marca','onblur':'validarMarca()'}),
            'categoria':forms.Select(attrs={'class':'form-control','id':'categoria','name':'categoria','onblur':'validarCategoria()'}),
            'precio':forms.NumberInput(attrs={'class':'form-control','id':'precio','name':'precio','onblur':'validarPrecio()'}),
            'encabezado':forms.TextInput(attrs={'class':'form-control','id':'encabezado','name':'encabezado','onblur':'validarEncabezado()'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control','id':'descripcion','name':'descripcion','onblur':'validarDescripcion()'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
            'info1':forms.TextInput(attrs={'class':'form-control','id':'info1','name':'info1','placeholder':'opcional'}),
            'info2':forms.TextInput(attrs={'class':'form-control','id':'info2','name':'info2','placeholder':'opcional'}),
            'info3':forms.TextInput(attrs={'class':'form-control','id':'info3','name':'info3','placeholder':'opcional'})
    }


class ContactoForm(ModelForm):
    class Meta:
        model = ContactoMensaje
        fields = [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'correo',
            'comentarios'
        ]
        labels = {
            'nombre':'Nombre',
            'apellidoPaterno':'Apellido Paterno',
            'apellidoMaterno':'Apellido Materno',
            'correo':'Correo Electronico',
            'comentarios':'Comentarios'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','id':'nombre','name':'nombre','onblur':'validarNombre()'}),
            'apellidoPaterno':forms.TextInput(attrs={'class':'form-control','id':'appaterno','name':'appaterno','onblur':'validarApellidoP()'}),
            'apellidoMaterno':forms.TextInput(attrs={'class':'form-control','id':'apmaterno','name':'apmaterno','onblur':'validarApellidoM()'}),
            'correo':forms.TextInput(attrs={'class':'form-control','id':'correo','name':'correo','onblur':'validarCorreo()'}),
            'comentarios':forms.Textarea(attrs={'class':'form-control','id':'comentarios','name':'comentarios','placeholder':'Ingrese sus comentarios','rows':'3','onblur':'validarComentarios()'})
        }