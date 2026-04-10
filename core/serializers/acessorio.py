from rest_framework import serializers

from core.models import Acessorio


class AcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorio
        fields = '__all__'