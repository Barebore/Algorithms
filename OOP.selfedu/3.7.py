import sys
from typing import Any


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ["old", "score"]:
            self.__dict__[__name] = int(__value)
        else:
            self.__dict__[__name] = __value

    def __bool__(self):
        if self.score > 0:
            return True
        else:
            return False
        
lst_in = list(map(str.strip, sys.stdin.readlines()))

players = []
for value in lst_in:
    players.append(Player(*value.split(';')))

players_filtered = list(filter(bool, players))
print(players_filtered)