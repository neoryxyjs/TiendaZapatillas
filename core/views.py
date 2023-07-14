from django.shortcuts import render,redirect
from crud.forms import *
from django.contrib import messages

# Create your views here.


def root(request):
    return redirect('index')

def index(request):

    context = {'Exclusivas':Zapatilla.objects.filter(categoria__nombreCategoria='Exclusiva'),
               'Deportivas':Zapatilla.objects.filter(categoria__nombreCategoria='Deportiva'),}

    return render(request,'core/index.html',context)

def nosotros(request):
    return render(request,'core/nosotros.html')

def contactanos(request):
    form = ContactoForm()
    context = {'form':form}
    if request.method == 'POST':
        form = ContactoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        else:
            return redirect(request.path)
    return render(request,'core/contactanos.html',context)

def ubicanos(request):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para ver nuestra ubicación.')
            return redirect('/login_app/')
    return render(request,'core/ubicanos.html')

def clima(request):
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para ver el detalle de la zapatilla')
            return redirect('/login_app/')
    return render(request,'core/clima.html')

def lanzamientos_recientes(request):
    context={'Recientes':Zapatilla.objects.all().order_by('-creacion')[:6]}
    return render(request,'core/lanzamientos_recientes.html',context)

def zapatillas(request):
    categorias = Categoria.objects.all()
    zapatillas_por_categoria = []

    filtro_categoria = request.GET.get('categoria')
    if filtro_categoria:
        categoria = Categoria.objects.get(id=filtro_categoria)
        zapatillas = Zapatilla.objects.filter(categoria=categoria)
        cantidad = zapatillas.count()
        zapatillas_por_categoria.append((categoria, zapatillas, cantidad))
    else:
        for categoria in categorias:
            zapatillas = Zapatilla.objects.filter(categoria=categoria)
            cantidad =  Zapatilla.objects.filter(categoria=categoria).count()
            zapatillas_por_categoria.append((categoria,zapatillas,cantidad))

    context = {'categorias':categorias,'zapatillas_por_categoria': zapatillas_por_categoria}
    return render(request,'core/zapatillas.html',context)

def zapatilla(request,id):
    zapatilla = Zapatilla.objects.get(id=id)
    context = {'zapatilla':zapatilla}
    if 'usuario' not in request.session:
            messages.error(request,'Debe iniciar sesión para ver el detalle de la zapatilla')
            return redirect('/login_app/')
    return render(request,'core/zapatilla.html',context)