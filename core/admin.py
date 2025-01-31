from django.contrib import admin

from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'data_evento', 'data_criacao', 'local_evento', 'usuario',)
    list_filter = ('titulo','data_evento',)

admin.site.register(Evento, EventoAdmin)