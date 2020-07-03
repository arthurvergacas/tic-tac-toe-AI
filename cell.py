class Cell:
    def __init__(self, x, y, w, h):
        self.x = x  # position
        self.y = y  # position
        self.w = w  # width of the cell
        self.h = h  # height of the cell
        self.state = ''  # state of the cell - can be '', 'X' or 'O'

    def checkUserCLicked(self, mousePos):
        x, y = mousePos

        if x >= self.x and x < self.x + self.w:
            if y >= self.y and y < self.y + self.h:
                return True

    def changeState(self, changeTo):
        # changeTo can be '', 'X' or 'O'
        # used to define the cell

        self.state = changeTo
