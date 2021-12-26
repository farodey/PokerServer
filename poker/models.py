from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255)
    pot = models.IntegerField()


class Player(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    chips = models.IntegerField()
    bb = models.BooleanField()
    sb = models.BooleanField()
    sitting_out = models.BooleanField()
    active = models.BooleanField()
    empty = models.BooleanField()


class Hand(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    card1 = models.CharField(max_length=5)
    card2 = models.CharField(max_length=5)


class Board(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    flop1 = models.CharField(max_length=5)
    flop2 = models.CharField(max_length=5)
    flop3 = models.CharField(max_length=5)
    tern = models.CharField(max_length=5)
    river = models.CharField(max_length=5)


