from cell import Cell
from graph2 import Vertex2


class DFS(object):
    def __init__(self, g, config):
        self.g = g
        self.discovered = set()
        self.mapping = {}
        self.path = []
        self.path_found = False
        start_cell = Cell(config['start_cell'][0], config['start_cell'][1])
        self.start_vertex = Vertex2(start_cell, 0)

    def search(self, v, target_vertex):
        if v == target_vertex:
            self.path_found = True
        self.discovered.add(v)
        for w in self.g.adj(v):
            if w not in self.discovered:
                self.mapping[v] = w
                self.search(w, target_vertex)

    def get_path(self, target_cell):
        #http://stackoverflow.com/questions/483666/python-reverse-inverse-a-mapping
        inv_mapping = {v: k for k, v in self.mapping.items()}
        path = [target_cell]
        while True:
            try:
                path.append(inv_mapping[path[-1]])
            except KeyError:
                break
        #http://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python
        return path[::-1]