from django.shortcuts import render, redirect, reverse
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.


def root(request):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    return redirect('index')

def lista_zapatillas(request):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    zapatillas = Zapatilla.objects.all();
    context = {'zapatillas':zapatillas}
    return render(request,'crud/lista_zapatillas.html',context)

def lista_categorias(request):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    categorias = Categoria.objects.all();
    context = {'categorias':categorias}
    return render(request,'crud/lista_categorias.html',context)

def lista_marcas(request):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    marcas = Marca.objects.all();
    context = {'marcas':marcas}
    return render(request,'crud/lista_marcas.html',context)

def nueva_categoria(request):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    form = CategoriaForm()
    context = {'form':form}
    if request.method == 'POST':
        form = CategoriaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        else:
            return redirect(request.path)
    return render(request,'crud/nueva_categoria.html',context)


def nueva_marca(request):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    form = MarcaForm()
    context = {'form':form}
    if request.method == 'POST':
        form = MarcaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        else:
            return redirect(request.path)
    return render(request,'crud/nueva_marca.html',context)

def nueva_zapatilla(request):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    form = ZapatillaForm()
    context = {'form':form}
    if request.method == 'POST':
        form = ZapatillaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        else:
            return redirect(request.path)
    return render(request,'crud/nueva_zapatilla.html',context)

def eliminar_zapatilla(request,idZapatilla):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    try:
        zapatilla = Zapatilla.objects.get(id = idZapatilla)
        zapatilla.delete()
        return redirect(reverse('lista_zapatillas'))
    except:
        return redirect(reverse('lista_zapatillas'))
        
def editar_zapatilla(request,idZapatilla):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    try:
        zapatilla = Zapatilla.objects.get(id = idZapatilla)
        form = ZapatillaForm(instance=zapatilla)
        if request.method == 'POST':
            form = ZapatillaForm(request.POST, request.FILES, instance=zapatilla)
            if form.is_valid():
                form.save()
                return redirect(request.path)
            else:
                return redirect(reverse('editar_zapatilla') + idZapatilla)

        context = {'form':form}
        return render(request,'crud/editar_zapatilla.html',context)
    except:
        return render(request,'crud/editar_zapatilla.html' + '?NO_EXIST')
    
def eliminar_categoria(request,idCategoria):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    try:
        categoria = Categoria.objects.get(id = idCategoria)
        categoria.delete()
        return redirect(reverse('lista_categorias'))
    except:
        return redirect(reverse('lista_categorias'))
        

def editar_categoria(request,idCategoria):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    try:
        categoria = Categoria.objects.get(id = idCategoria)
        form = CategoriaForm(instance=categoria)
        if request.method == 'POST':
            form = CategoriaForm(request.POST, request.FILES, instance=categoria)
            if form.is_valid():
                form.save()
                return redirect(request.path)
            else:
                return redirect(reverse('editar_categoria') + idCategoria)

        context = {'form':form}
        return render(request,'crud/editar_categoria.html',context)
    except:
        return render(request,'crud/editar_categoria.html')
    
def eliminar_marca(request,idMarca):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    try:
        marca = Marca.objects.get(id = idMarca)
        marca.delete()
        return redirect(reverse('lista_marcas'))
    except:
        return redirect(reverse('lista_marcas'))

def editar_marca(request,idMarca):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    try:
        marca = Marca.objects.get(id = idMarca)
        form = MarcaForm(instance=marca)
        if request.method == 'POST':
            form = MarcaForm(request.POST, request.FILES, instance=marca)
            if form.is_valid():
                form.save()
                return redirect(request.path)
            else:
                return redirect(reverse('editar_categoria') + idMarca)

        context = {'form':form}
        return render(request,'crud/editar_marca.html',context)
    except:
        return render(request,'crud/editar_marca.html')

def lista_comentarios(request):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para acceder a esta página.')
            return redirect('/login_app/')
    
    if request.session['usuario'].get('rol') != 'STAFF':
       messages.error(request,'Debe ser un usuario STAFF para acceder a esta página.')
       return redirect('/login_app/success')
    
    comentarios = ContactoMensaje.objects.all();
    context = {'comentarios':comentarios}
    return render(request,'crud/lista_comentarios.html',context)
    