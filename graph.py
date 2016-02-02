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
            if '<Vertex cell=<Cell col=%r,row=%r>,alt=%r>' % (e[0][0], e[0][1], e[0][2]) not in self.vertices:
                orig = Vertex(cell=Cell(col=e[0][0], row=e[0][1]), alt=e[0][2])
            else:
                orig = self.get_vertex(col=e[0][0], row=e[0][1], alt=e[0][2])

            if '<Vertex cell=<Cell col=%r,row=%r>,alt=%r>' % (e[1][0], e[1][1], e[1][2]) not in self.vertices:
                dest = Vertex(cell=Cell(col=e[1][0], row=e[1][1]), alt=e[1][2])
            else:
                dest = self.get_vertex(col=e[1][0], row=e[1][1], alt=e[1][2])

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


def movement(orig, vel, num_cols):
    next_r = orig[0] + vel[0]
    next_c = (orig[1] + vel[1]) % num_cols
    return Cell(row=next_r, col=next_c)


def construct_graph(config):
    edges = []
    for a in range(config['A']):
        for r in range(config['R']):
            for c in range(config['C']):
                cell_orig = Cell(row=r, col=c)
                wind_velocity = config['a_map'][a][r][c]
                cell_dest = movement(orig=cell_orig, vel=wind_velocity, num_cols=config['C'])

                v_orig = Vertex(cell=cell_orig, alt=a)
                v_dest = Vertex(cell=cell_dest, alt=a)
                edges.append(Edge(v_orig, v_dest))

    return Graph(edges=edges)
