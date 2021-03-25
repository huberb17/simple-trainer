import os
import time
from abc import ABC
from random import randint

from simple_trainer.file_handler import (GameFileHandler, PlayerFileHandler,
                                         StatsFileHandler)
from simple_trainer.game import Games, MiniAddGame, MiniMultiGame
from simple_trainer.player import Player
from simple_trainer.stats import GameStats
from simple_trainer.utils import clear, int_input, str_input


class GameBoard:
    """Central game class, holds players, games and statistics.
    """    
    def __init__(self, path: str):
        self.data_path : str = path
        self.players : list = None
        self.games : list = None
        self.stats : list = None

    def load_games(self, game_handler: GameFileHandler) -> list:
        self.games = Games(self.data_path, game_handler)
        return self.games
        
    def set_stats_handler(self, stats_handler: StatsFileHandler) -> GameStats:
        self.stats_handler = stats_handler
        self.stats_handler.set_datafile(os.path.join(self.data_path, 'stats.data'))
        self.stats = self.stats_handler.load()
        return self.stats

    def load_players(self, player_handler: PlayerFileHandler) -> list:
        self.player_handler = player_handler
        self.player_handler.set_datafile(os.path.join(self.data_path, 'players.data'))
        self.players = self.player_handler.load()
        return self.players

    def add_player(self, name : str) -> Player:
        self.players.append(Player(name, 0))
        return self.players[len(self.players)-1]

    def store_result(self):
        self.player_handler.store(self.players)
        self.stats_handler.store(self.stats.stats)


class ResultManager:
    pass


def main():
    game_board = GameBoard('data')
    players = game_board.load_players(PlayerFileHandler())
    games = game_board.load_games(GameFileHandler())
    stats = game_board.set_stats_handler(StatsFileHandler())

    clear()
    if not players:
        name = str_input('Gib Spielernamen ein: ')
        player = game_board.add_player(name)
    else:
        print('Wähle Spieler:')
        last_index = 0
        for player in players:
            print(f'[{players.index(player)}]: {player.name} ({player.highscore})')
            last_index = players.index(player)
        print(f'[{last_index + 1}]: Neuen Spieler anlegen')
        print(f'[{last_index + 2}]: Beenden')
        choice = int_input('Auswahl: ')
        if choice > last_index + 1:
            exit(0)
        elif choice > last_index:
            name = str_input('Gib Spielernamen ein: ')
            player = game_board.add_player(name)
        else:
            player = players[choice]
    
    print(f'Hallo {player.name}, los geht es!')
    end_game = False
    while not end_game:
        print('Wähle Spiel: ')
        for game in games:
            print(f'[{games.index(game)}]: {game.name}')
        choice = int_input('Auswahl: ')
        if choice >= len(games) - 1:
            choice = len(games) - 1
        current_game = games[choice]
        
        turns = []
        while len(turns) < 10:
            index = randint(0, len(current_game.calculations)-1)
            if index not in turns:
                turns.append(index)

        ov_start = time.time()
        ov_correct = 0
        for turn in turns:
            start = time.time()
            result = int_input(f'{current_game.get_calc(turn)} = ')
            end = time.time()
            elapsed = end - start
            if current_game.solve_calc(turn, result):
                print('Korrekt!')
                player.increase_highscore(1)
                stats.add(player.name, current_game.name, turn, True, elapsed)
                ov_correct += 1
            else:
                print('Leider falsch')
                player.decrease_highscore(1)
                stats.add(player.name, current_game.name, turn, False, elapsed)
        ov_end = time.time()
        ov_time = ov_end - ov_start
        print(f'Statistik dieser Runde:')
        print(f'------------------------------------------------------------------')
        print(f'{len(turns)} Rechnungen, davon {ov_correct} richtig.')
        print(f'{round(ov_time,2)} Sekunden für diese Aufgabe (ca. {round(ov_time/len(turns),2)} Sekunden pro Rechnung).')
        print(f'{player.name}, dein neuer Highscore ist: {player.highscore} Punkte.')
        game_board.store_result()
        choice = str_input('Willst du nochmal spielen? [j/n]: ')
        if choice.lower() != 'j':
            end_game = True


if __name__ == "__main__":
    main()
