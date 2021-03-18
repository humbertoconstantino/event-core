from django.db import models
#Importando User para usar chave estranheira
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_event = models.DateTimeField()
    date_create = models.DateTimeField(auto_now=True, verbose_name='Creation Date')
    #Chave estrangeira
    user = models.ForeignKey(User, on_delete=models.CASCADE)#CASCADE = SE O USUARIO FOR DELETADO, EXCLUIR SEUS EVENTOS JUNTO COM ELE.


#Definindo nome da table

    class Meta:
        db_table = 'event'

    #Mudando event object p/ titulo
    def __str__(self):
        return self.title






