import logging
import json
import copy
import random
from itertools import chain

from django.shortcuts import render
from channels import Group

from sudoku.models import GameUser, Game
from sudoku.generator import make_board

from ciscosparkapi import CiscoSparkAPI


logger = logging.getLogger(__name__)


def new(request, token, email):
    user, created = GameUser.objects.get_or_create(access_token=token, email=email)

    solved = make_board()
    unsolved = copy.deepcopy(solved)
    unsolved[random.randint(0, 8)][random.randint(0, 8)] = 0
    unsolved[random.randint(0, 8)][random.randint(0, 8)] = 0
    unsolved[random.randint(0, 8)][random.randint(0, 8)] = 0

    unsolved_json = json.dumps(list(chain.from_iterable(unsolved)))
    solved_json = json.dumps(list(chain.from_iterable(solved)))

    game = Game.objects.create(user1=user, board=unsolved_json, board_solved=solved_json)

    messages = CiscoSparkAPI().messages
    messages.create(toPersonEmail='lauzhack-lewis-test@sparkbot.io',
                    text=json.dumps({"game_id": game.pk, "token": token, "email": email}))

    return render(request, 'waiting.html', {"game_id": game.pk, "token": token, "email": email})


def save_game(request, token_id):
    pass


def add_user(request):
    pass


def play(request, game_id):
    game = Game.objects.get(pk=game_id)
    return render(request, 'game.html', {
        'board': game.board,
        'board_solved': game.board_solved,
        'access_token': game.user1.access_token,
        'email': game.user2.email,
        'game_id': game_id
    })


def join(request, game_id, email, token):
    user2, created = GameUser.objects.get_or_create(access_token=token, email=email)

    game = Game.objects.get(pk=game_id)
    game.user2 = user2
    game.save()

    Group("chat-%s" % game_id).send({"text": "start"})

    return render(request, 'game.html', {
        'board': game.board,
        'board_solved' : game.board_solved,
        'access_token': game.user2.access_token,
        'email': game.user1.email,
        'game_id': game_id
    })
