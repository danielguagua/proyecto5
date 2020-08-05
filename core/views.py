from django.http import HttpResponse
from django.shortcuts import render

# Create your views here

html_base = """
    <h1>Mi Primer Menu</h1>
    <ul>
        <li>   <a href="/">Home</a>              </li>
        <li>   <a href="/about/"> Acerca de: </a>   </li>
        <li>   <a href="/contact/"> Contacto </a>     </li>
        <li>   <a href="/quienes_somos/"> quienes </a>     </li>
        <li>   <a href="/servicios/"> nuestros servicios son: </a>     </li>
    </ul>
"""


def home(request):
    html_responsde = "<h1>La pagina de portada</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def contact(request):
    html_responsde = "<h1>La pagina de contacto</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def about(request):
    html_responsde = "<h1>la pagina de Acerca De</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def quienes_somos(request):
    html_responsde = "<h1>La pagina de quienes somos</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def servicios(request):
    html_responsde = "<h1>La pagina de servicio</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def home(request, template="home.html"):
    return render(request, template)

def about(request, template="about.html"):
    return render(request, template)

def contact(request, template="contact.html"):
    return render(request, template)

def quienes_somos(request, template="quienes_somos.html"):
    return render(request, template)

def servicios(request, template="servicios.html"):
    return render(request, template)




def login(request):
    html_responsde = "<h1>La pagina de login</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def login(request, template="login1.html"):
    return render(request, template)

def inventario(request):
    html_responsde = "<h1>La pagina de inventario</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def inventario(request, template="inventario.html"):
    return render(request, template)


def usuarios(request):
    html_responsde = "<h1>La pagina de inventario</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde)

def usuarios(request, template="usuarios.html"):
    return render(request, template)
