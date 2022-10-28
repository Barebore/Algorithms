import random
random.seed(4)
rr = random.randint

class Cell:
    def __init__(self, mine, around_mines = 0):
        self.around_mines = around_mines #число мин вокруг клетки
        self.mine = mine #наличие мины в текущей клетке(булево)
        self.fl_open = False  #открыта или закрыта клетка

class GamePole:
    def __init__(self, N, M):
        self.init(N,M)

    def init(self, N, M):
        self.N = N #размер поля
        self.M = M #общее количество мин на поле
        self.pole = [[0 for i in range(self.N)] for j in range(self.N)]
        for i in range(N):
            for j in range(N):
                self.pole[i][j] = Cell(False)
        self.cache = M
        while self.cache > 0:
            x = rr(0, self.N-1)
            y = rr(0, self.N-1)
            if self.pole[x][y].mine == False:
                self.pole[x][y].mine = True
                self.cache -= 1
                try:
                    if x - 1 >= 0 and y - 1 >= 0:
                        self.pole[x-1][y-1].around_mines += 1
                except:
                    pass
                try:
                    if x - 1 >= 0:
                        self.pole[x-1][y].around_mines += 1
                except:
                    pass
                try:
                    if x - 1 >= 0:
                        self.pole[x-1][y+1].around_mines += 1
                except:
                    pass
                try:
                    if y - 1 >= 0:
                        self.pole[x][y-1].around_mines += 1
                except:
                    pass
                try:
                    self.pole[x][y+1].around_mines += 1
                except:
                    pass
                try:
                    if y - 1 >= 0:
                        self.pole[x+1][y-1].around_mines += 1
                except:
                    pass
                try:
                    self.pole[x+1][y].around_mines += 1
                except:
                    pass
                try:
                    self.pole[x+1][y+1].around_mines += 1
                except:
                    pass
            
    def show(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole)):
                if self.pole[i][j].fl_open == True:
                    print(self.pole[i][j].around_mines, end = ' ')
                else:
                    print('#', end = ' ')
            print()
    def show2(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole)):
                if self.pole[i][j].mine == True:
                    print('*', end = ' ')
                #elif self.pole[i][j].around_mines > 0:
                else:
                    print(self.pole[i][j].around_mines, end = ' ') 
            print()

#c1 = Cell(around_mines, mine)

pole_game = GamePole(10, 12)
#pole_game.show()
pole_game.show2()