# Autonomous Delivery Agent in 2D Grid (CLI)

A Python CLI project simulating an autonomous delivery agent navigating a 2D city grid, handling static/dynamic obstacles and varying terrain, using multiple search/replanning strategies.

## Features

- Models static obstacles, dynamic obstacles, and varying terrain costs
- Rational agent: maximizes delivery efficiency under time/fuel constraints
- Implements BFS, Uniform-cost, A* (with admissible heuristic), and local search (hill climbing)
- CLI for running and comparing experiments
- Experimental results: path cost, nodes expanded, time
- Analysis of algorithm performance

## Usage

```bash
python main.py --map maps/map1.txt --algo astar --time 100 --fuel 100
```

## Map Format

- `S` = Start, `G` = Goal
- `.` = normal terrain, `#` = wall/obstacle, `M` = mountain (5x cost), `W` = water (10x cost)

Example:
```
S...
.M#.
..GW
```

## Extending

- Add your own maps in the `maps/` directory.
- Add more algorithms or dynamic obstacle handling in `agent/algorithms.py`.

## Requirements

See `requirements.txt`.

## Analysis

- Run multiple algorithms on various maps and compare path cost, nodes expanded, and time.
- See results in CLI output and write your own analysis in `results/` or report file.
