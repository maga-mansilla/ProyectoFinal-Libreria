from django.http import HttpResponse

def saludo (request):
    return HttpResponse("<h1> ¡hola! </h1><p> soy maga.</p>")

def inicio(request):
    return HttpResponse("Vista inicio")