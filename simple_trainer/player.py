class Player:
    def __init__(self, name, highscore):
        self.name = name
        self.highscore = int(highscore)

    def increase_highscore(self, amount):
        self.highscore += amount

    def decrease_highscore(self, amount):
        self.highscore -= amount
