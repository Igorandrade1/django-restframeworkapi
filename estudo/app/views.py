from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from app.serializers import PessoaSerializer
from app.models import Pessoa
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# Create your views here.



class Pessoa_methodos(APIView):

    def get(self, request):
        pessoa = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoa, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Pessoa_methodos_seg(APIView):
    def get_object(self, pk):
        try:
            return Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            raise NotFound()


    def get(self, request, pk):
        pessoa = self.get_object(pk)
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    def put(self, request, pk):
        pessoa = self.get_object(pk=pk)
        serializer = PessoaSerializer(pessoa, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

