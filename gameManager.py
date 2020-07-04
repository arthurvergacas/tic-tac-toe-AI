class GameManager:
    def __init__(self):
        self.currentPlayer = 'X'
        # can be either X's turn or O's turn
        # X goes first cause yes
        # can also be '', which means that the game is over

        self.gameState = ''
        # game state can be:
        # progress - the game is in progress
        # over - the game ended

        self.result = ''
        # the result of the game can be:
        # X - X won
        # O - O won
        # tie - no winners

    def changeTurn(self):
        # to change turn faster
        # basically the function is here so i dont accidentally screw over my logic

        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'

    def checkWin(self, board, returnWinner=False):
        # dumb method to check if there's a win can't think sorry ;-;

        won = False

        rowTop = [board[0], board[3], board[6]]
        rowMid = [board[1], board[4], board[7]]
        rowBot = [board[2], board[5], board[8]]

        columnLeft = [board[0], board[1], board[2]]
        columnMid = [board[3], board[4], board[5]]
        columnRight = [board[6], board[7], board[8]]

        leftToRightDiag = [board[0], board[4], board[8]]
        rightToLeftDiag = [board[6], board[4], board[2]]

        allGames = [rowTop, rowMid, rowBot,
                    columnLeft, columnMid, columnRight,
                    leftToRightDiag, rightToLeftDiag]

        for game in allGames:
            if game[0].state == game[1].state and game[0].state == game[2].state and game[0].state != '':
                won = True
                if returnWinner:
                    return game[0].state
                else:
                    return won

    def checkTie(self, board):

        for cell in board:
            if cell.state == '':
                return False

        return True
