from django.shortcuts import render

def index(request):
    return render(request, 'productos/index.html')

def listaproductos(request):
    return render(request, 'productos/listaproductos.html')
