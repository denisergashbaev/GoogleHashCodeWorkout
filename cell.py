class Cell(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return '<Cell row=%r,col=%r>' % (self.row, self.col)