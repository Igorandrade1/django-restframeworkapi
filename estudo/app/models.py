from wsgiref.validate import validator
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Pessoa(models.Model):
    SEXO_CHOICES = [
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Não binario"),
        ("P", "Prefiro não dizer")
    ]
    
    nome = models.CharField(max_length=100, blank=False, null=False)
    idade = models.IntegerField(blank=True, null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


