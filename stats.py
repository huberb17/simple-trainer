class TurnStat:
    def __init__(self, overall=0, positive=0, overall_time=0.0, avg_time = 0.0):
        super().__init__()
        self.overall = overall
        self.positive = positive
        self.overall_time = overall_time
        self.avg_time = avg_time

    def __str__(self):
        return f'Overall: {self.overall}, Positive: {self.positive}, Overall time: {self.overall_time}, Avg. time: {self.avg_time}'

class GameStats:
    def __init__(self):
        super().__init__()
        self.stats = {}
    
    def add(self, player, game, turn, correct, elapsed_time):
        player_stat = {}
        if player in self.stats.keys():
            player_stat = self.stats[player]
        game_stat = {}
        if game in player_stat.keys():
            game_stat = player_stat[game]
        turn_stat = TurnStat()
        if turn in game_stat.keys():
            turn_stat = game_stat[turn]
        turn_stat.overall += 1
        if correct: turn_stat.positive += 1
        turn_stat.overall_time += elapsed_time
        turn_stat.avg_time = turn_stat.overall_time / turn_stat.overall
        game_stat[turn] = turn_stat
        player_stat[game] = game_stat
        self.stats[player] = player_stat

    def __str__(self):
        res = ''
        for x in self.stats.keys():
            res += x + '\n'
            player_stats = self.stats[x]
            for y in player_stats.keys():
                res += y + '\n'
                game_stats = player_stats[y]
                for z in game_stats.keys():
                    res += f'[{z}]: {game_stats[z]}\n'
        return res

