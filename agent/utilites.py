# Placeholder for any utilities (e.g., random map generation, stats output)
import random

def random_map(width, height, obstacle_prob=0.2):
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            if random.random() < obstacle_prob:
                row.append('#')
            else:
                row.append('.')
        grid.append(''.join(row))
    grid[0] = 'S' + grid[0][1:]
    grid[-1] = grid[-1][:-1] + 'G'
    return '\n'.join(grid)
