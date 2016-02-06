class Cell(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @staticmethod
    def load_all_cells(config):
        cells = []
        for r in range(config['R']):
            for c in range(config['C']):
                cells.append(Cell(r, c))
        return cells

    @staticmethod
    def load_target_cells(config):
        cells = []
        for r, c in config['targets']:
            cells.append(Cell(r, c))
        return cells

    #http://stackoverflow.com/questions/4901815/object-of-custom-type-as-dictionary-key
    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)

    def __repr__(self):
        return '<Cell row=%r,col=%r>' % (self.row, self.col)