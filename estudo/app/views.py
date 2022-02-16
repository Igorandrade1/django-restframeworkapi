from app.serializers import PessoaSerializer
from app.models import Pessoa
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# Create your views here.

#apirest
class PessoaViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer



