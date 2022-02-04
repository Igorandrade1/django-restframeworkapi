from app.models import Pessoa


from rest_framework import serializers

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['nome','idade','sexo','created_at']