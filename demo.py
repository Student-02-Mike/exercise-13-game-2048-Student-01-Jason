import random


class Game():
    def __init__(self):
        self.list = [[0] * 4 for _ in range(4)]
        self.score = 0

    def print(self):
        for i in self.list:
            for j in i:
                print(j, end='\t')
            print('')

    def update(self):
        for i in range(4):
            for j in range(4):
                if self.list[i][j] == 0:
                    self.list[i][j] = random.choice([0, 2, 4])

    def tidy(self):
        new = [[0] * 4 for _ in range(4)]
        for i in range(4):
            temp = 0
            for j in range(4):
                if self.list[i][j] != 0:
                    new[i][temp] = self.list[i][j]
                    temp += 1
        self.list = new

    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.list[i][j] == self.list[i][j + 1]:
                    self.list[i][j] *= 2
                    self.list[i][j + 1] = 0

    def reverse(self):
        for i in range(4):
            for j in range(2):
                self.list[i][j], self.list[i][3 - j] = self.list[i][3 - j], self.list[i][j]

    def change(self):
        new = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new[i][j] = self.list[j][i]
        self.list = new

    def tidy_combine(self):
        self.tidy()
        self.combine()
        self.tidy()

    def left(self):
        self.tidy_combine()

    def right(self):
        self.reverse()
        self.tidy_combine()
        self.reverse()

    def up(self):
        self.change()
        self.tidy_combine()
        self.change()

    def down(self):
        self.change()
        self.reverse()
        self.tidy_combine()
        self.reverse()
        self.change()

    def operate(self, cmd):
        #TODO

    def start(self):
        self.update()
        while (True):
            self.print()
            cmd = input('Please input command: a,d,w,s (left,right,up,down)\n')
            self.operate(cmd)
            self.update()


game = Game()
game.start()
