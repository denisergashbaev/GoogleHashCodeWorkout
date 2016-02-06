import read_input_file
import balloon_manager
from cell import Cell
from graph2 import Graph2, Vertex2

config = read_input_file.load_configuration('test_input')
selected_targets = balloon_manager.select_targets(config)
balloons = balloon_manager.assign_balloons(config, selected_targets)

#Pablo's dirty code
#g = graph.construct_graph(config)


g = Graph2(config)

if False:
    for r in range(config['R']):  # For all rows
        for c in range(config['C']):  # For all columns
            v = Vertex2(Cell(r, c), 2)
            adj = g.adj(v)
            print "Adjacent cells for vertex %s are: %s" % (v, adj)
