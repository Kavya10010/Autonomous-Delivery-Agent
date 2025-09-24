import argparse
from agent.environment import GridEnvironment
from agent.agent import DeliveryAgent
from agent.algorithms import bfs, uniform_cost_search, a_star, hill_climbing
import time

def run_experiment(map_file, algorithm, max_time, max_fuel):
    env = GridEnvironment.from_file(map_file)
    agent = DeliveryAgent(env, max_time=max_time, max_fuel=max_fuel)
    
    start = time.time()
    if algorithm == 'bfs':
        result = bfs(agent)
    elif algorithm == 'ucs':
        result = uniform_cost_search(agent)
    elif algorithm == 'astar':
        result = a_star(agent)
    elif algorithm == 'hill':
        result = hill_climbing(agent)
    else:
        raise ValueError("Unknown algorithm")
    elapsed = time.time() - start

    print(f"Algorithm: {algorithm}")
    print(f"Path cost: {result['cost']}")
    print(f"Nodes expanded: {result['nodes_expanded']}")
    print(f"Execution time: {elapsed:.3f} seconds")
    print(f"Path: {result['path']}")
    return {
        'algorithm': algorithm,
        'cost': result['cost'],
        'nodes_expanded': result['nodes_expanded'],
        'time': elapsed
    }

def main():
    parser = argparse.ArgumentParser(description="Autonomous Delivery Agent on 2D Grid")
    parser.add_argument('--map', type=str, help='Path to map file', required=True)
    parser.add_argument('--algo', type=str, choices=['bfs','ucs','astar','hill'], required=True)
    parser.add_argument('--time', type=int, default=100, help='Max time allowed')
    parser.add_argument('--fuel', type=int, default=100, help='Max fuel allowed')
    args = parser.parse_args()
    
    run_experiment(args.map, args.algo, args.time, args.fuel)

if __name__ == "__main__":
    main()
