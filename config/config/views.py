from django .http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from datetime import datetime
from random import randint

def saludo(request):
    return HttpResponse("Hola Mundo - desde Django")

def segunda_vista(request):
    return HttpResponse("<h1>Esta es una segunda vista</h1>")

def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"Hola {nombre} {apellido}")

def probando_templates(request):
    '''
    Es necesario importarlas clases context y templates:
    from django.template import Context, Template
    '''
    mi_html = open('./templates/template1.html', encoding='utf-8')
    mi_template = Template(mi_html.read())
    mi_html.close()
    nombre = 'Gabriel'
    apellido = 'Galiano'
    datos = {"nombre" : nombre, "apellido": apellido}
    mi_contexto = Context(datos)
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)

def probando_templates_render(request):
    nombre = 'Gabriel'
    apellido = 'Galiano'
    fecha = datetime.now()
    datos = {"nombre" : nombre, "apellido": apellido, 'fecha': fecha}
    return render(request, "template1.html", context=datos)

def probando_templates2(request):
    lista_de_notas = [1,2,3,4,5,6,7,8,9,10]
    contexto = {"notas": lista_de_notas}
    return render(request, "template2.html", context=contexto)

def probando_template3(request):
    numero_random = randint(1, 10)
    contexto = {"numero_random": numero_random}
    return render(request, "template3.html", context=contexto)

def index(request):
    return render(request, "index.html")