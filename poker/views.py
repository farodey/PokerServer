from django.shortcuts import render
from rest_framework import generics
from poker.serializers import GameStatusSerializer


class GameStatusView(generics.GenericAPIView):
    serializer_class = GameStatusSerializer
