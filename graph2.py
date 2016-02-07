from cell import Cell


class Vertex2(object):
    def __init__(self, cell, alt):
        self.cell = cell
        self.alt = alt

    #http://stackoverflow.com/questions/4901815/object-of-custom-type-as-dictionary-key
    def __hash__(self):
        return hash((self.cell, self.alt))

    def __eq__(self, other):
        return (self.cell, self.alt) == (other.cell, other.alt)


    def __repr__(self):
        return '<Vertex cell=%r,alt=%r>' % (self.cell, self.alt)


class Graph2(object):
    def __init__(self, config):
        self.config = config
        self.g = {}

        A = config['A']
        for a in range(A):  # For all height levels
            next_a_min, next_a_max = max(a-1, 1), min(a+2, A)
            for r in range(self.config['R']):  # For all rows
                for c in range(self.config['C']):  # For all columns
                    vertex_orig = Vertex2(Cell(r, c), a)
                    for next_a in range(next_a_min, next_a_max):  # For all height levels the balloon can move
                        vertex_dest = self._movement(vertex_orig, next_a)
                        if vertex_dest:
                            self._add_edge(vertex_orig, vertex_dest)

    def _movement(self, vertex_orig, next_a):
        vel = self.config['a_map'][next_a - 1][vertex_orig.cell.row][vertex_orig.cell.col]
        next_r = vertex_orig.cell.row + vel[0]
        vertex_dest = None
        # Check if destination cell is out of range
        if 0 <= next_r < self.config['R']:
            next_c = (vertex_orig.cell.col + vel[1]) % self.config['C']
            vertex_dest = Vertex2(Cell(next_r, next_c), next_a)
        return vertex_dest

    def _init_and_get(self, v):
        try:
            return self.g[v]
        except KeyError:
             self.g[v] = set()
        return self.g[v]

    def _add_edge(self, v, w):
        self._init_and_get(v).add(w)

    def adj(self, v):
        return self._init_and_get(v)
