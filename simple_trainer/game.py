from abc import ABC
from .file_handler import PlayerFileHandler, GameFileHandler

class Games(list):
    def __init__(self):
        super().__init__()
        self.append(MiniAddGame('Plusrechnen', 'MiniAdd.data'))
        self.append(MiniMultiGame('Kleines Einmal Eins', 'MiniMulti.data'))
        self.append(MediSubGame('Subraktionen', 'MediSub.data'))

class Game(ABC):
    def get_calc(self, index):
        pass
    def solve_calc(self, index, result):
        pass

class MiniMultiGame(Game):
    def __init__(self, name, file_name):
        super().__init__()
        self.name = name
        self.calculations = GameFileHandler(file_name).load()
        if not self.calculations:
            for x in range(1, 11):
                for y in range(1, 11):
                    self.calculations.append((f'{x} * {y}', x*y))
            GameFileHandler(file_name).store(self.calculations)
    
    def get_calc(self, index):
        if index < 0: intex = 0
        if index >= len(self.calculations): index = len(self.calculations) - 1
        return self.calculations[index][0]

    def solve_calc(self, index, result):
        if result == int(self.calculations[index][1]): return True
        else: return False

class MiniAddGame(Game):
    def __init__(self, name, file_name):
        super().__init__()
        self.name = name
        self.calculations = GameFileHandler(file_name).load()
        if not self.calculations:
            for x in range(0, 21):
                for y in range(0, 21):
                    if x + y <= 20:
                        self.calculations.append((f'{x} + {y}', x+y))
            GameFileHandler(file_name).store(self.calculations)
    
    def get_calc(self, index):
        if index < 0: intex = 0
        if index >= len(self.calculations): index = len(self.calculations) - 1
        return self.calculations[index][0]

    def solve_calc(self, index, result):
        if result == int(self.calculations[index][1]): return True
        else: return False

class MediSubGame(Game):
    def __init__(self, name, file_name):
        super().__init__()
        self.name = name
        self.calculations = GameFileHandler(file_name).load()
        if not self.calculations:
            for x in range(0, 151):
                for y in range(0, 151):
                    if x - y >= 0:
                        self.calculations.append((f'{x} - {y}', x-y))
            GameFileHandler(file_name).store(self.calculations)
    
    def get_calc(self, index):
        if index < 0: intex = 0
        if index >= len(self.calculations): index = len(self.calculations) - 1
        return self.calculations[index][0]

    def solve_calc(self, index, result):
        if result == int(self.calculations[index][1]): return True
        else: return False
