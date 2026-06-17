
from objects import Player
from utils import PLAYER_CLASS
from .tools import register


@register(PLAYER_CLASS, PLAYER_CLASS)
def Player2Player(player1: Player, player2: Player):
    if not player1.is_alive() or not player2.is_alive():
        return
    player1.damage(3)
    player2.damage(3)
    