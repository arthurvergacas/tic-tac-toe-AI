import random # only for development purposes

class Ai:
    def __init__(self, board):
        self.board = board
    
    def play(self):
        # choose a cell to play 
        chosen = random.choice(self.board)
        while chosen.state != '':
            chosen = random.choice(self.board)
        chosen.state = 'O'
