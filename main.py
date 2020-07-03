import pygame
from cell import Cell

class MainGUI:
    def __init__ (self):
        pygame.init()

        pygame.display.set_caption("Tic Tac Toe")

        self.WIDTH = 540
        self.HEIGHT = 540
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.background.fill(pygame.Color('#ffffff'))


        self.cellWidth = self.WIDTH / 3
        self.cellHeight = self.HEIGHT/ 3
        self.grid = []

        # to create the 3x3 grid 
        for i in range(3):
            for j in range(3):
                self.grid.append(Cell(self.cellWidth * i, self.cellHeight * j, self.cellWidth, self.cellHeight))
        


        self.running = True

    def displayGrids(self):
        
        # horizontal lines
        for i in range(2):
            # pygame.draw.line(surface, color, start_pos, end_pos, width = 1)
            start_pos = (0, int(self.cellHeight * (i + 1)))
            end_pos = (self.WIDTH, int(self.cellHeight * (i + 1)))
            pygame.draw.line(self.background, (0, 0, 0), start_pos, end_pos)
        
        # vertical lines
        for i in range(2):
            # pygame.draw.line(surface, color, start_pos, end_pos, width = 1)
            start_pos = (int(self.cellWidth * (i + 1)), 0)
            end_pos = (int(self.cellWidth * (i + 1)), self.HEIGHT)
            pygame.draw.line(self.background, (0, 0, 0), start_pos, end_pos)
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # check mouse down -- user input
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for cell in self.grid:
                        if cell.checkUserCLicked(pygame.mouse.get_pos()) and cell.state == '':
                            cell.changeState('X') # cause only the O player is the AI
                            

                            

            self.screen.blit(self.background, (0, 0))   
            self.displayGrids()         

            pygame.display.update()
            



if __name__ == "__main__":
    clss = MainGUI()

    clss.run()






