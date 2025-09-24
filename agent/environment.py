import numpy as np

class GridEnvironment:
    def __init__(self, grid, start, goal, terrain_costs, dynamic_obstacles=None):
        self.grid = grid  # 2D numpy array
        self.start = tuple(start)
        self.goal = tuple(goal)
        self.terrain_costs = terrain_costs
        self.dynamic_obstacles = dynamic_obstacles or []

    @staticmethod
    def from_file(filename):
        grid, start, goal, terrain_costs = [], None, None, {}
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                row = []
                for j, cell in enumerate(line.strip()):
                    if cell == 'S':
                        start = (i, j)
                        row.append('.')
                    elif cell == 'G':
                        goal = (i, j)
                        row.append('.')
                    else:
                        row.append(cell)
                grid.append(row)
        grid = np.array(grid)
        # Terrain cost mapping
        terrain_costs = {'.': 1, '#': float('inf'), 'M': 5, 'W': 10}  # .:normal, #:wall, M:mountain, W:water
        return GridEnvironment(grid, start, goal, terrain_costs)

    def is_valid(self, x, y):
        if 0 <= x < self.grid.shape[0] and 0 <= y < self.grid.shape[1]:
            return self.grid[x, y] != '#'
        return False

    def get_cost(self, x, y):
        return self.terrain_costs.get(self.grid[x, y], 1)

    def neighbors(self, pos):
        x, y = pos
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if self.is_valid(nx, ny):
                yield (nx, ny)
