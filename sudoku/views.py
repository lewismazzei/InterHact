import logging
import json
import copy
import random
from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import SuspiciousOperation
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


def play(request, game_id):
    game = Game.objects.get(pk=game_id)
    return render(request, 'game.html', {
        'board': game.board,
        'board_solved': game.board_solved,
        'access_token': game.user1.real_access_token,
        'email': game.user2.email,
        'game_id': game_id
    })


def join(request, game_id, email, token, room):
    user2, created = GameUser.objects.get_or_create(access_token=token)
    user2.email = email
    user2.room = room
    user2.save()

    game = Game.objects.get(pk=game_id)
    game.user2 = user2
    game.save()

    Group("chat-%s" % game_id).send({"text": "start"})

    return render(request, 'game.html', {
        'board': game.board,
        'board_solved' : game.board_solved,
        'access_token': game.user2.real_access_token,
        'email': game.user1.email,
        'game_id': game_id
    })


def save(request, game_id, token, score):
    game = Game.objects.get(pk=game_id)
    if game.user1 and game.user1.access_token == token:
        print("saving first user")
        game.user1_points = score
        game.save()
    elif game.user2 and game.user2.access_token == token:
        print("saving second user")
        game.user2_points = score
        game.save()
    else:
        raise SuspiciousOperation()

    if game.user1_points is not None and game.user2_points is not None:
        print('Sending the results to bot')
        messages = CiscoSparkAPI().messages
        messages.create(toPersonEmail='lauzhack-lewis-test@sparkbot.io',
                        text=json.dumps({
                            "user1": {
                                "points": game.user1_points,
                                "token": game.user1.access_token,
                                "email": game.user1.email,
                                "room": game.user1.room,
                            },
                            "user2": {
                                "points": game.user2_points,
                                "token": game.user2.access_token,
                                "email": game.user2.email,
                                "room": game.user2.room,
                            },
                        }))
        # messages.create(toPersonEmail=game.user1.email,
        #                 text="You got %d" % game.user1_points)
        # messages.create(toPersonEmail=game.user2.email,
        #                 text="You got %d" % game.user2_points)

    return HttpResponse()


def results(request):
    games = Game.objects.order_by('-pk')
    return render(request, 'results.html', {'games': games})


def patients(request):
    users = GameUser.objects.all()
    return render(request, 'patients.html', {'patients': users})
