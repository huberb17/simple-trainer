import os
from abc import ABC

from .file_handler import GameFileHandler, PlayerFileHandler


class Games(list):
    def __init__(self, path: str, game_handler: GameFileHandler):
        super().__init__()
        self.append(MiniAddGame(game_handler, 'Plusrechnen', os.path.join(path,'MiniAdd.data')))
        self.append(MiniMultiGame(game_handler, 'Kleines Einmal Eins', os.path.join(path, 'MiniMulti.data')))
        self.append(MediSubGame(game_handler, 'Subraktionen', os.path.join(path, 'MediSub.data')))

class Game(ABC):
    def get_calc(self, index):
        pass
    def solve_calc(self, index, result):
        pass

class MiniMultiGame(Game):
    def __init__(self, game_handler, name, file_name):
        super().__init__()
        self.name = name
        game_handler.set_datafile(file_name)
        self.calculations = game_handler.load()
        if not self.calculations:
            for x in range(1, 11):
                for y in range(1, 11):
                    self.calculations.append((f'{x} * {y}', x*y))
            game_handler.store(self.calculations)
    
    def get_calc(self, index):
        if index < 0: index = 0
        if index >= len(self.calculations): index = len(self.calculations) - 1
        return self.calculations[index][0]

    def solve_calc(self, index, result):
        if result == int(self.calculations[index][1]): return True
        else: return False

class MiniAddGame(Game):
    def __init__(self, game_handler, name, file_name):
        super().__init__()
        self.name = name
        game_handler.set_datafile(file_name)
        self.calculations = game_handler.load()
        if not self.calculations:
            for x in range(0, 21):
                for y in range(0, 21):
                    if x + y <= 20:
                        self.calculations.append((f'{x} + {y}', x+y))
            game_handler.store(self.calculations)
    
    def get_calc(self, index):
        if index < 0: index = 0
        if index >= len(self.calculations): index = len(self.calculations) - 1
        return self.calculations[index][0]

    def solve_calc(self, index, result):
        if result == int(self.calculations[index][1]): return True
        else: return False

class MediSubGame(Game):
    def __init__(self, game_handler, name, file_name):
        super().__init__()
        self.name = name
        game_handler.set_datafile(file_name)
        self.calculations = game_handler.load()
        if not self.calculations:
            for x in range(0, 151):
                for y in range(0, 151):
                    if x - y >= 0:
                        self.calculations.append((f'{x} - {y}', x-y))
            game_handler.store(self.calculations)
    
    def get_calc(self, index):
        if index < 0: index = 0
        if index >= len(self.calculations): index = len(self.calculations) - 1
        return self.calculations[index][0]

    def solve_calc(self, index, result):
        if result == int(self.calculations[index][1]): return True
        else: return False
