from cell import Cell


class Blob(object):
    def __init__(self, top_left_coords, bottom_right_coords):
        self.min_p = top_left_coords
        self.max_p = bottom_right_coords
        self.grid = []
        for r in range(self.min_p[1], self.max_p[1] + 1):
            row = []
            for c in range(self.min_p[0], self.max_p[0] + 1):
                cell = Cell(r, c, r == c)
                row.append(cell)
            self.grid.append(row)


def find_blobs(config):
    G = config.grid

    for r in range(1, config.grid.rows):
        current_color = 0
        for c in range(1, config.grid.cols):
            if G[r][c].marked:
                neighbours_list = config.get_marked_neighbours(r, c)

                if not neighbours_list:
                    current_color += 1
                    G[r][c].color = current_color
                    G[r][c].parent_color = current_color
                else:
                    neighbours_color = map(lambda x: x.color, neighbours_list)
                    min_color = min(neighbours_color)

                    G[r][c].color = min_color
                    G[r][c].parent_color = min_color

                    for n in neighbours_list:
                        if n.color > min_color:
                            G[n.row][n.col].parent_color = min_color
    return G
