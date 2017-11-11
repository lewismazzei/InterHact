from django.shortcuts import render


def create_game(request, token):
    return


def save_game(request, token_id):
    pass


def add_user(request):
    pass


def show_board(request, game_id, token):

    return render(request, 'game.html')
