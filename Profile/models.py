
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import re

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    bith_date = models.DateField()
    cpf = models.CharField(max_length=11)
    address= models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    state =models.CharField(max_length=2,
    choices=(('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),))

    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name}'

    def clean(self):
        error_messages = {}
        if re.search(r'^[0-9]', self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'cep inválido, por favor digite os 8 números do seu cep'

        if error_messages:
            raise ValidationError(error_messages)
            
