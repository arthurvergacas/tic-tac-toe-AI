import pygame
from cell import Cell
from gameManager import GameManager
from ai import Ai


class MainGUI:
    def __init__(self):
        pygame.init()

        self.manager = GameManager()
        self.enemy = Ai()

        pygame.display.set_caption("Tic Tac Toe")

        self.WIDTH = 540
        self.HEIGHT = 540
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.background.fill(pygame.Color('#E3E3E3'))

        self.playerFont = pygame.font.SysFont('arial', 70)

        self.cellWidth = self.WIDTH / 3
        self.cellHeight = self.HEIGHT / 3
        self.board = []

        # to create the 3x3 grid
        for i in range(3):
            for j in range(3):
                self.board.append(
                    Cell(self.cellWidth * i, self.cellHeight * j, self.cellWidth, self.cellHeight))

        self.manager.gameState = 'progress'

        self.running = True

    def displayGrids(self):

        # horizontal lines
        for i in range(2):
            # pygame.draw.line(surface, color, start_pos, end_pos, width = 1)
            start_pos = (0, int(self.cellHeight * (i + 1)))
            end_pos = (self.WIDTH, int(self.cellHeight * (i + 1)))
            pygame.draw.line(self.background, (0, 0, 0),
                             start_pos, end_pos, 2)

        # vertical lines
        for i in range(2):
            # pygame.draw.line(surface, color, start_pos, end_pos, width = 1)
            start_pos = (int(self.cellWidth * (i + 1)), 0)
            end_pos = (int(self.cellWidth * (i + 1)), self.HEIGHT)
            pygame.draw.line(self.background, (0, 0, 0),
                             start_pos, end_pos, 2)

        for cell in self.board:
            player = self.playerFont.render(cell.state, True, (0, 0, 0))
            x, y = self.playerFont.size(cell.state)
            self.screen.blit(
                player, (int((cell.x + cell.w / 2) - x / 2), int((cell.y + cell.h / 2) - y / 2)))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # check mouse down
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.manager.gameState == 'progress':
                        for cell in self.board:
                            if self.manager.currentPlayer == 'X' and cell.checkUserCLicked(pygame.mouse.get_pos()) and cell.state == '':
                                # cause the O player is the AI
                                cell.changeState('X')
                                self.manager.changeTurn()

                # check keys pressed
                if event.type == pygame.KEYDOWN:
                    # restart the game
                    if event.key == pygame.K_r and self.manager.gameState == 'over':
                        self.manager.currentPlayer = 'X'
                        for cell in self.board:
                            cell.state = ''
                        self.manager.gameState = 'progress'

                    # recolorize the background
                    self.background.fill(pygame.Color('#ffffff'))

            # to check if there's a win
            if self.manager.checkWin(self.board):
                self.manager.currentPlayer = ''
                self.manager.gameState = 'over'
                self.manager.result = self.manager.checkWin(self.board, True)

            # to check if there's a tie
            if self.manager.checkTie(self.board):
                self.manager.currentPlayer = ''
                self.manager.gameState = 'over'
                self.manager.result = 'tie'

            # check if it's AI turn
            if self.manager.currentPlayer == 'O' and self.manager.gameState == 'progress':
                self.enemy.play(self.board)
                self.manager.changeTurn()

            # UI
            if self.manager.gameState == 'over':
                # if tie, paint te background gray
                if self.manager.result == 'tie':
                    self.background.fill(pygame.Color('#9DA897'))
                elif self.manager.result == 'X':
                    self.background.fill(pygame.Color('#7AFF77'))
                elif self.manager.result == 'O':
                    self.background.fill(pygame.Color('#F53920'))

                self.displayGrids()

            self.screen.blit(self.background, (0, 0))

            self.displayGrids()

            pygame.display.update()


if __name__ == "__main__":
    clss = MainGUI()

    clss.run()
