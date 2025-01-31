from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
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
    except Exception as e:
        return HttpResponse('Não foi possível realizar a consulta')

@login_required(login_url='/login/')
def lista_eventos(request):
    try:
        user = request.user
        data_atual = datetime.now() - timedelta(hours=1)
        evento = Evento.objects.filter(usuario=user,
                                    data_evento__gt=data_atual)
        dados = {'eventos': evento}
    except Exception as e:
        raise Http404
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento =  request.GET.get('id')
    dados = {}
    if id_evento:
        try:
            dados['evento'] = Evento.objects.get(id=id_evento)
        except Exception as e:
            raise Http404
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        local_evento = request.POST.get('local_evento')
        usuario = request.user
        id_evento =  request.POST.get('id_evento')

        if id_evento:
            try:
                evento = Evento.objects.get(id=id_evento)
            except Exception as e:
                raise Http404()
            if evento.usuario == usuario:
                evento.titulo=titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.local_evento = local_evento
                evento.save()
                #Evento.objects.filter(id=id_evento).update(titulo=titulo,
                #                                           descricao = descricao,
                #                                           data_evento = data_evento,
                #                                           local_evento = local_evento)
            else:
                raise Http404()
            return redirect('/')

        else:
            Evento.objects.create(titulo=titulo,
                                descricao = descricao,
                                data_evento = data_evento,
                                local_evento = local_evento,
                                usuario = usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception as e:
       raise Http404
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404
    return redirect('/')


def json_lista_evento(request, id_usuario):
    try:
        usuario = User.objects.get(id=id_usuario)
        evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo', 'descricao')
    except Exception as e:
        raise Http404
    return JsonResponse(list(evento), safe=False)

@login_required(login_url='/login/')
def log_eventos(request):
    try:
        usuario = request.user
        evento = Evento.objects.filter(usuario=usuario)
        dados = {'eventos':evento}
    except Exception as e:
        Http404
    return render(request, 'log.html', dados)