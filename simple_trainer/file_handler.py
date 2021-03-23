from abc import ABC
import os
from player import Player
from stats import TurnStat, GameStats

class FileHandler(ABC):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
    def load(self):
        pass
    def store(self):
        pass

class PlayerFileHandler(FileHandler):
    def __init__(self, file_name):
        super().__init__(file_name)
        
    def load(self):
        if not os.path.exists(self.file_name): return []
        content = []
        with open(self.file_name) as f:
            content = f.readlines()
        # name; 
        return [Player(x.strip().split(';')[0], x.strip().split(';')[1]) for x in content]

    def store(self, players):
        with open(self.file_name, 'w') as f:
            f.writelines([f'{x.name};{x.highscore}\n' for x in players])


class GameFileHandler(FileHandler):
    def __init__(self, file_name):
        super().__init__(file_name)
        
    def load(self):
        if not os.path.exists(self.file_name): return []
        content = []
        with open(self.file_name) as f:
            content = f.readlines()
        # name; 
        return [(x.strip().split(';')[0], x.strip().split(';')[1]) for x in content]

    def store(self, calcs):
        with open(self.file_name, 'w') as f:
            f.writelines([f'{x[0]};{x[1]}\n' for x in calcs])

class StatsFileHandler(FileHandler):
    def __init__(self, file_name):
        super().__init__(file_name)

    def load(self):
        if not os.path.exists(self.file_name): return GameStats()
        content = []
        with open(self.file_name) as f:
            content = f.readlines()
        stats = {}
        player_stats = {}
        game_stats = {}
        for x in content:
            player, game, turn, overall, positive, ov_time, avg_time = x.strip().split(';')
            turn_stat = TurnStat(overall, positive, ov_time, avg_time)
            game_stats[turn] = turn_stat
            player_stats[game] = game_stats
            stats[player] = player_stats
        game_stats = GameStats()
        game_stats.stats = stats
        return game_stats

    def store(self, stats):
        with open(self.file_name, 'w') as f:
            for x in stats.keys():
                player_stats = stats[x]
                for y in player_stats.keys():
                    game_stats = player_stats[y]
                    for z in game_stats.keys():
                        turn_stat = game_stats[z]
                        res = f'{x};{y};{z};{turn_stat.overall};{turn_stat.positive};{turn_stat.overall_time};{turn_stat.avg_time}\n'
                        f.write(res)