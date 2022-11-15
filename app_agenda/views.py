from django.shortcuts import render, HttpResponse
from app_agenda.models import Evento

# Create your views here.
def hello(request):
    return HttpResponse('<h1>hello</h1>')


def lista_eventos(request):
    evento = Evento.objects.all()
    data = ({'evento': evento})
    return render(request, 'agenda.html', data)
