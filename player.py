import random
from abc import ABCMeta, abstractmethod
from typing import List

from board import Board


class Player(metaclass=ABCMeta):
    def __init__(self, player_id: int):
        self.player_id = player_id

    @abstractmethod
    def act(self, board: Board) -> int:
        pass


class RandomPlayer(Player):
    """Choose grid randomly."""

    def act(self, board: Board) -> int:
        candidates: List = list(board.get_players_movable_grids(self.player_id).keys())
        return random.choice(candidates)
