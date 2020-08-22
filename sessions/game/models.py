from django.db import models


class Player(models.Model):
    player_id = models.CharField(primary_key=True)


class Game(models.Model):
    game_id = models.CharField(primary_key=True)


class PlayerGameInfo(models.Model):
    pass
