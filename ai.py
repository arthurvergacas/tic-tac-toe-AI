import random
from gameManager import GameManager


class Ai:
    def __init__(self):

        self.manager = GameManager()

    def minimax(self, board, OPlayer, alpha, beta, depth=float('inf')):
        # return the static evaluation of the final possible game
        # X wins: -1
        # O wins: +1
        # tie: 0

        if depth == 0 or self.manager.checkWin(board) or self.manager.checkTie(board):
            if self.manager.checkWin(board, True) == 'X':
                return -1
            elif self.manager.checkWin(board, True) == 'O':
                return 1
            elif self.manager.checkTie(board):
                return 0
            else:
                return True

        if OPlayer:
            maxValue = float('-inf')
            for cell in board:
                if cell.state == '':
                    cell.state = 'O'
                    value = self.minimax(
                        board, False, alpha, beta, depth=depth - 1)
                    cell.state = ''
                    maxValue = max(maxValue, value)
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        break

            return maxValue

        if OPlayer == False:
            minValue = float('inf')
            for cell in board:
                if cell.state == '':
                    cell.state = 'X'
                    value = self.minimax(
                        board, True, alpha, beta, depth=depth - 1)
                    cell.state = ''
                    minValue = min(minValue, value)
                    beta = min(beta, value)
                    if beta <= alpha:
                        break
            return minValue

    def play(self, board):
        # choose a cell to play

        # initializing move to store the best cell to move
        bestCell = None
        bestScore = float('-inf')

        for cell in board:
            if cell.state == '':
                cell.state = 'O'
                score = self.minimax(board, False, float(
                    '-inf'), float('inf'), depth=1)
                cell.state = ''

                if isinstance(score, bool) == False:
                    if score > bestScore:
                        bestScore = score
                        bestCell = cell
                else:
                    bestCell = random.choice(board)
                    while bestCell.state != '':
                        bestCell = random.choice(board)

        bestCell.changeState('O')
