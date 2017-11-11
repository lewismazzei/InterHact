import json
import logging
import json
import copy
import random
from itertools import chain

from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation

from sudoku.models import GameUser, Game
from sudoku.generator import make_board

from ciscosparkapi.api.messages import MessagesAPI


logger = logging.getLogger(__name__)


def create_game(request, token, email):
    user, created = GameUser.objects.get_or_create(access_token=token, email=email)

    solved = make_board()
    unsolved = copy.deepcopy(solved)
    unsolved[random.randint(0, 8)][random.randint(0, 8)] = 0
    unsolved[random.randint(0, 8)][random.randint(0, 8)] = 0
    unsolved[random.randint(0, 8)][random.randint(0, 8)] = 0

    unsolved_json = json.dumps(list(chain.from_iterable(unsolved)))
    solved_json = json.dumps(list(chain.from_iterable(solved)))

    Game.objects.create(user1=user, board=unsolved_json, board_solved=solved_json)

    return render(request, 'waiting.html')


def save_game(request, token_id):
    pass


def add_user(request):
    pass


def show_board(request, game_id, token):
    game = Game.objects.get(pk=game_id)
    return render(request, 'game.html', {
        'board': game.board,
        'board_solved' : game.board_solved
    })
