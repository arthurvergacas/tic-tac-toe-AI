class GameManager:
    def __init__(self):
        self.currentPlayer = 'X' # can be either X's turn or O's turn
                                 # X goes first cause yes

    def changeTurn(self):
        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'
    
    def checkWin(self, grid):
        # dumb method to check if there's a win can't think sorry ;-;

        won = False

        rowTop = [grid[0], grid[3], grid[6]]
        rowMid = [grid[1], grid[4], grid[7]]
        rowBot = [grid[2], grid[5], grid[8]]

        columnLeft = [grid[0], grid[1], grid[2]]
        columnMid = [grid[3], grid[4], grid[5]]
        columnRight = [grid[6], grid[7], grid[8]]

        leftToRightDiag = [grid[0], grid[4], grid[8]]
        rightToLeftDiag = [grid[6], grid[4], grid[2]]

        allGames = [rowTop, rowMid, rowBot, 
                columnLeft, columnMid, columnRight, 
                leftToRightDiag, rightToLeftDiag]
            
        for game in allGames:
            if game[0].state == game[1].state and game[0].state == game[2].state and game[0].state != '':
                won = True
                break

        
        return won
                


        

