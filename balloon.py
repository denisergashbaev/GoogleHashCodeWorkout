class Balloon(object):
    def __init__(self, index, target_cell):
        self.index = index
        self.target_cell = target_cell

    def __repr__(self):
        return '<Balloon index=%r,target_cell=%r>' % (self.index, self.target_cell)