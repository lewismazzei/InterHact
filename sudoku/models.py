from django.db import models


class GameUser(models.Model):
    access_token = models.CharField(max_length=255)
    email = models.EmailField(blank=True)


class Game(models.Model):
    user1 = models.ForeignKey(GameUser, related_name='user1_rel')
    user2 = models.ForeignKey(GameUser, related_name='user2_rel', blank=True)
    user1_points = models.IntegerField(null=True, blank=True)
    user2_points = models.IntegerField(null=True, blank=True)
    board = models.TextField(null=True, blank=True)
    board_solved = models.TextField(null=True, blank=True)
