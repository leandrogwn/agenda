from django.shortcuts import redirect, render, HttpResponse

from core.models import Evento

# Create your views here.

#def index(request):
#    return redirect('/agenda/')

def local(request, titulo_evento):
    try:
        evento = Evento.objects.get(titulo=titulo_evento)
        local = evento.local_evento
        return HttpResponse('O local do evento {} sera no {}. '.format(titulo_evento, local))
    except:
        return HttpResponse('Não foi possível realizar a consulta')

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}

    return render(request, 'agenda.html', dados)
