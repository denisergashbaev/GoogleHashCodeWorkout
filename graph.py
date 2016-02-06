from cell import Cell


class Vertex(object):
    def __init__(self, cell, alt):
        self.cell = cell
        self.alt = alt

    def __repr__(self):
        return '<Vertex cell=%r,alt=%r>' % (self.cell, self.alt)


class Edge(object):
    def __init__(self, orig, dest):
        self.orig = orig
        self.dest = dest

    def __repr__(self):
        return '<Edge orig=%r,dest=%r>' % (self.orig, self.dest)


class Graph(object):
    def __init__(self, edges=()):

        self.vertices = {}
        self.edges = {}
        for e in edges:
            if '<Vertex cell=<Cell col=%r,row=%r>,alt=%r>' % (e.dest.cell.col, e.dest.cell.row, e.dest.alt) not in self.vertices:
                dest = Vertex(cell=Cell(col=e.dest.cell.col, row=e.dest.cell.row), alt=e.dest.alt)
            else:
                dest = self.get_vertex(col=e.dest.cell.col, row=e.dest.cell.row, alt=e.dest.alt)

            if '<Vertex cell=<Cell col=%r,row=%r>,alt=%r>' % (e.orig.cell.col, e.orig.cell.row, e.orig.alt) not in self.vertices:
                orig = Vertex(cell=Cell(col=e.orig.cell.col, row=e.orig.cell.row), alt=e.orig.alt)
            else:
                orig = self.get_vertex(col=e.orig.cell.col, row=e.orig.cell.row, alt=e.orig.alt)

            self.add_edge(orig=orig, dest=dest)

    def add_vertex(self, alt, cell=None, col=None, row=None):
        if cell is not None:
            v = Vertex(cell=cell, alt=alt)
        else:
            v = Vertex(cell=Cell(col=col, row=row), alt=alt)

        self.vertices[v.__repr__()] = v

    def add_edge(self, orig, dest):
        e = Edge(orig=orig, dest=dest)
        self.edges[e.__repr__()] = e

    def get_vertex(self, col, row, alt):
        return self.vertices['<Vertex cell=<Cell col=%r,row=%r>,alt=%r>' % (col, row, alt)]

    def get_edge(self, orig, dest):
        return self.vertices['<Vertex orig=%r,dest=%r>' % (orig, dest)]


def movement(row_orig, col_orig, vel, num_cols):
    next_r = row_orig + vel[0]
    next_c = (col_orig + vel[1]) % num_cols
    return Cell(row=next_r, col=next_c)


def construct_graph(config):
    edges = []
    for a in range(config['A']):  # For all high levels

        for r in range(config['R']):  # For all rows

            for c in range(config['C']):  # For all columns

                for possible_level in range(max(a-1, 1), min(a+2, config['A'])):  # For all high levels the balloon can move

                    wind_velocity = config['a_map'][possible_level][r][c]
                    cell_dest = movement(row_orig=r, col_orig=c, vel=wind_velocity, num_cols=config['C'])

                    # Check if destination cell is out of range
                    if 0 <= cell_dest.row < config['R']:
                        cell_orig = Cell(row=r, col=c)
                    else:
                        continue

                    v_orig = Vertex(cell=cell_orig, alt=a)
                    v_dest = Vertex(cell=cell_dest, alt=possible_level)
                    edges.append(Edge(v_orig, v_dest))

    return Graph(edges=edges)
