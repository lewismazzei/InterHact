import json
import logging
import json
import copy
import random

from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation

from sudoku.models import GameUser, Game
from sudoku.generator import make_board


logger = logging.getLogger(__name__)


def create_game(request, token, email):
    user, created = GameUser.objects.get_or_create(access_token=token, email=email)

    solved = make_board()
    unsolved = copy.deepcopy(solved)
    solved[random.randint(0, 8)][random.randint(0, 8)] = 0
    solved[random.randint(0, 8)][random.randint(0, 8)] = 0
    solved[random.randint(0, 8)][random.randint(0, 8)] = 0

    Game.objects.create(user1=user, board=json.dumps(unsolved), board_solved=json.dumps(solved))
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
