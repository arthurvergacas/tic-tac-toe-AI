from gameManager import GameManager


class Ai:
    def __init__(self):

        self.manager = GameManager()

    def minimax(self, board, OPlayer, depth=float('inf')):
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
                return 0

        if OPlayer:
            maxValue = float('-inf')
            for cell in board:
                if cell.state == '':
                    cell.state = 'O'
                    value = self.minimax(board, False, depth=depth - 1)
                    cell.state = ''
                    maxValue = max(maxValue, value)
            return maxValue

        if OPlayer == False:
            minValue = float('inf')
            for cell in board:
                if cell.state == '':
                    cell.state = 'X'
                    value = self.minimax(board, True, depth=depth - 1)
                    cell.state = ''
                    minValue = min(minValue, value)
            return minValue

    def play(self, board):
        # choose a cell to play

        # initializing move to store the best cell to move
        bestCell = None
        bestScore = float('-inf')

        for cell in board:
            if cell.state == '':
                cell.state = 'O'
                score = self.minimax(board, False)
                cell.state = ''

                if score > bestScore:
                    bestScore = score
                    bestCell = cell

        bestCell.changeState('O')
