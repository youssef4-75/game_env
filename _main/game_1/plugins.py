import pygame as pg

from animation import Animation
from game import GameManager

from objects import Player

from utils import consolify
from plugins import WithBackGround, WithPDisplayer
from utils import Vector, PLAYER_SIZE
from utils import from_root



def main(game):
    disp = WithPDisplayer()
    bg = WithBackGround(from_root("assets/bg1.png"))
    game.add_plugin(bg, disp)