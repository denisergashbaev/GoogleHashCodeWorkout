class Cell(object):
    def __init__(self, row, col, marked):
        self.row = row
        self.col = col
        self.marked = marked

    #http://stackoverflow.com/questions/4901815/object-of-custom-type-as-dictionary-key
    def __hash__(self):
        return hash((self.row, self.col, self.marked))

    def __eq__(self, other):
        return (self.row, self.col, self.marked) == (other.row, other.col, self.marked)

    def __repr__(self):
        return '<Cell row=%r,col=%r, marked=%r>' % (self.row, self.col, self.marked)