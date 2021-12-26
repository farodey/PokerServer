from rest_framework import serializers
from poker.models import Game


class GameStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
