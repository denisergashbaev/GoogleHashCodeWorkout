from hashcode2016.cell import Cell
from hashcode2016.file_utils import get_line


class Config(object):
    def __init__(self, config_file):
        self.grid = []
        with open(config_file, 'r') as f:
            self.rows, self.cols = get_line(f.readline())
            for row_index in range(self.rows):
                data = f.readline()
                row = []
                for col_index, c in enumerate(data):
                    cell = Cell(row_index, col_index, c == '#')
                    row.append(cell)
                self.grid.append(row)

    def get_marked_neighbours(self, row, col):
        neigbours_list = []
        for r in range(max(row-1, 0), min(row+2, self.rows), 2):
            for c in range(max(col-1, 0), min(col+2, self.cols), 2):
                if self.grid[r][c].marked and self.grid[r][c].color is not None:
                    neigbours_list.append(self.grid[r][c])
        return neigbours_list
