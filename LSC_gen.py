import copy
import random

import numpy as np
from latinsq import LatinSquare


class LSC():

    def __init__(self, n, t=None):
        """
        This generator works by generating a Latin square of order nxn and then slowly removing the needed percentages
        from the same Latin square that way it keeps the result with less noise.

        :param n: size of Latin square that need to be generated
        :param t: list of the percentages of the cells that you want to remove from the Latin square
        """
        if t is None:
            t = [0.1, 0.2, 0.3]
        self.difficulty = sorted(t)
        self.n = n
        self.ls = LatinSquare().random(self.n)
        self.solution = copy.deepcopy(self.ls)
        self.choose = list(range(self.n ** 2))

    def turn_to_list(self):
        ls = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                ls[i][j] = self.ls[i, j]
        return ls

    def puzzle_mode(self, mode=0):
        """
        :param mode: percentage you want to remove in a loop over all the percentages (Look at the example)
        :return: LSC with zero in place of the removed cells
        """
        if mode == 0:
            remove_cells = int(self.n ** 2 * self.difficulty[mode])
        else:
            remove_cells = int(self.n ** 2 * (self.difficulty[mode] - self.difficulty[mode - 1]))
        to_remove = random.sample(self.choose, remove_cells)
        for t in to_remove:
            i = t // self.n
            j = t % self.n
            self.ls[i, j] = 0
            self.choose.remove(t)
        return self.turn_to_list()
