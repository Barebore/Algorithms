class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    pass


c1 = Cell(around_mines, mine)