from balloon import Balloon
from cell import Cell
import random


def select_targets(config):
    target_count = config['L']
    balloon_count = config['B']
    #all_cells = Cell.load_all_cells(config)
    target_cells = Cell.load_target_cells(config)
    selected_targets = random.sample(target_cells, balloon_count) if balloon_count < target_count else target_cells
    return selected_targets


def assign_balloons(config, target_cells):
    balloons = []
    for i in range(config['B']):
        balloon = Balloon(i, target_cells[i % len(target_cells)])
        balloons.append(balloon)
    return balloons
