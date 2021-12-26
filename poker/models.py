from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255)
    pot = models.IntegerField()


class Player(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    chips = models.IntegerField()
    game_position = models.IntegerField()
    sitting_out = models.BooleanField()


class Hand(models.Model):
    player = models.ManyToManyField(Player)
    card1 = models.CharField(max_length=5)
    card2 = models.CharField(max_length=5)


class Board(models.Model):
    game = models.ManyToManyField(Game)
    flop1 = models.CharField(max_length=5)
    flop2 = models.CharField(max_length=5)
    flop3 = models.CharField(max_length=5)
    tern = models.CharField(max_length=5)
    river = models.CharField(max_length=5)


