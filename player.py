import random
from abc import ABCMeta, abstractmethod
from typing import Dict, List

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
        candidates: List = list(board.get_players_movable_grids(player_id=self.player_id).keys())
        return random.choice(candidates)


class Human(Player):
    """Grid is chosen by human interactively."""

    def act(self, board: Board) -> int:
        candidates: Dict = board.get_players_movable_grids(player_id=self.player_id)
        while True:
            raw_input = input(f"You can choose from {candidates}: ")
            try:
                result = int(raw_input)
            except ValueError:
                print(f"Invalid input {result}. Input should be Integer.")
                continue
            if result not in candidates:
                print(f"Invalid input {result}. Input should be from {list(candidates.keys())}.")
                continue
            return result
