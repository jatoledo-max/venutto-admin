from django.shortcuts import render
from .models import Producto

def menu(request):
    productos = Producto.objects.filter(disponible=True)
    contexto = {
        "productos":productos,
    }
    return render(request,
                "productos/menu.html",
                contexto,
        )