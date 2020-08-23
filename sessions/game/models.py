from django.db import models


class Player(models.Model):
    player_id = models.CharField(max_length=10, primary_key=True)


class Game(models.Model):
    game_id = models.CharField(max_length=10, primary_key=True)
    number = models.CharField(max_length=1, )


class PlayerGameInfo(models.Model):
    pass
