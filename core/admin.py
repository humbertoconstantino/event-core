from django.contrib import admin
from core.models import Event
# Register your models here.

#Configurar o parametro list_display para aparecer na listagem
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_event', 'date_create')
    list_filter = ('user', 'date_event')

admin.site.register(Event, EventAdmin)

