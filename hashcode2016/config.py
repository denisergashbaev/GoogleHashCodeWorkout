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