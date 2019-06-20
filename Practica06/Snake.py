import numpy as np

class Snake:
    def __init__(self, x=0, y=0,):
        self.pos = [[x, y]]
        self.direcc = 0

    def mover(self):
        for ii in np.arange(len(self.pos) - 1, 0, -1):
            self.pos[ii] = self.pos[ii - 1][:]

        if self.direcc == 0:
            self.pos[0][0] += 1
        if self.direcc == 1:
            self.pos[0][1] += 1
        if self.direcc == 2:
            self.pos[0][0] -= 1
        if self.direcc == 3:
            self.pos[0][1] -= 1