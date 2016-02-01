import math


class Balloon(object):
    def __init__(self, index, config, target_cell=None):
        self.index = index
        self.config = config
        self.current_cell = config['start_cell']
        self.target_cell = target_cell
        self.level = 0
        self.lost = False

    def apply_wind(self, wind):
        if not self.lost:
            self.current_cell = (self.current_cell[0] + wind[0], (self.current_cell[1] + wind[1]) % self.config['C'])
            self.lost = not (0 <= self.current_cell[0] < self.config['R'])

    def calc_targets_covered(self):
        targ_covered_count = 0
        if not self.lost:
            for target in self.config['targets']:
                if (self.current_cell[0] - target[0])**2 + self._column_dist(self.current_cell[1], target[1])**2 <= self.config['V']**2:
                    targ_covered_count += 1
        return targ_covered_count

    def _column_dist(self, c1, c2):
        return min(math.fabs(c1-c2), self.config['C'] - math.fabs(c1-c2))

    def __repr__(self):
        return '<Balloon-%r: current_cell=%r,level=%s,target_cell=%r,lost=%s>' % \
               (self.index, self.current_cell, self.level, self.target_cell, self.lost)