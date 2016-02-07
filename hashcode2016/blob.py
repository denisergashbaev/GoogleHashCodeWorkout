from cell import Cell


class Blob(object):
    def __init__(self):
        self.min_p = (0, 0)
        self.max_p = (4, 4)
        self.grid = []
        for r in range(self.min_p[1], self.max_p[1] + 1):
            row = []
            for c in range(self.min_p[0], self.max_p[0] + 1):
                cell = Cell(r, c, r == c)
                row.append(cell)
            self.grid.append(row)
