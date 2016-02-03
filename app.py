import read_input_file
import balloon_manager
import graph

config = read_input_file.load_configuration('test_input')
selected_targets = balloon_manager.select_targets(config)
balloons = balloon_manager.assign_balloons(config, selected_targets)

g = graph.construct_graph(config)