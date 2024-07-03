from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from core.models import Evento

# Create your views here.

#def index(request):
#    return redirect('/agenda/')

def login_user(request):
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário ou senha inválida.")
    return redirect('/')

def local(request, titulo_evento):
    try:
        evento = Evento.objects.get(titulo=titulo_evento)
        local = evento.local_evento
        return HttpResponse('O local do evento {} sera no {}. '.format(titulo_evento, local))
    except:
        return HttpResponse('Não foi possível realizar a consulta')

@login_required(login_url='/login/')
def lista_eventos(request):
    user = request.user
    evento = Evento.objects.filter(usuario=user)
    dados = {'eventos': evento}

    return render(request, 'agenda.html', dados)
