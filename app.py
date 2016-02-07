import read_input_file
import balloon_manager
from cell import Cell
from dfs import DFS
from graph2 import Graph2, Vertex2

config = read_input_file.load_configuration('test_input')
selected_targets = balloon_manager.select_targets(config)
balloons = balloon_manager.assign_balloons(config, selected_targets)

g = Graph2(config)
dfs = DFS(g, config)
for balloon in balloons:
    target_vertex = Vertex2(balloon.target_cell, 1)
    dfs.search(dfs.start_vertex, target_vertex)
    print "start_vertex: %s, target_vertex: %s" % (dfs.start_vertex, target_vertex)
    print "path found: %s" % dfs.path_found
    print "path: %s" % dfs.get_path(target_vertex)

if False:
    for r in range(config['R']):  # For all rows
        for c in range(config['C']):  # For all columns
            v = Vertex2(Cell(r, c), 2)
            adj = g.adj(v)
            print "Adjacent cells for vertex %s are: %s" % (v, adj)
