import heapq
from collections import deque

def bfs(agent):
    env = agent.env
    start, goal = env.start, env.goal
    queue = deque([(start, [start])])
    visited = set()
    nodes_expanded = 0

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        nodes_expanded += 1
        if state == goal:
            return {'path': path, 'cost': len(path)-1, 'nodes_expanded': nodes_expanded}
        for neighbor in env.neighbors(state):
            if neighbor not in visited:
                queue.append((neighbor, path+[neighbor]))
    return {'path': [], 'cost': float('inf'), 'nodes_expanded': nodes_expanded}

def uniform_cost_search(agent):
    env = agent.env
    start, goal = env.start, env.goal
    heap = [(0, start, [start])]
    visited = {}
    nodes_expanded = 0

    while heap:
        cost, state, path = heapq.heappop(heap)
        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost
        nodes_expanded += 1
        if state == goal:
            return {'path': path, 'cost': cost, 'nodes_expanded': nodes_expanded}
        for neighbor in env.neighbors(state):
            ncost = cost + env.get_cost(*neighbor)
            heapq.heappush(heap, (ncost, neighbor, path+[neighbor]))
    return {'path': [], 'cost': float('inf'), 'nodes_expanded': nodes_expanded}

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star(agent):
    env = agent.env
    start, goal = env.start, env.goal
    heap = [(heuristic(start, goal), 0, start, [start])]
    visited = {}
    nodes_expanded = 0

    while heap:
        est, cost, state, path = heapq.heappop(heap)
        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost
        nodes_expanded += 1
        if state == goal:
            return {'path': path, 'cost': cost, 'nodes_expanded': nodes_expanded}
        for neighbor in env.neighbors(state):
            ncost = cost + env.get_cost(*neighbor)
            heur = heuristic(neighbor, goal)
            heapq.heappush(heap, (ncost+heur, ncost, neighbor, path+[neighbor]))
    return {'path': [], 'cost': float('inf'), 'nodes_expanded': nodes_expanded}

import random

def hill_climbing(agent, max_iters=1000, restarts=5):
    env = agent.env
    goal = env.goal
    best_path, best_cost = None, float('inf')
    nodes_expanded = 0
    for _ in range(restarts):
        state = env.start
        path = [state]
        cost = 0
        for _ in range(max_iters):
            neighbors = list(env.neighbors(state))
            if not neighbors:
                break
            # Pick neighbor with lowest cost+heuristic
            random.shuffle(neighbors)
            next_state = min(neighbors, key=lambda n: env.get_cost(*n) + heuristic(n, goal))
            if next_state == goal:
                path.append(next_state)
                cost += env.get_cost(*next_state)
                break
            path.append(next_state)
            cost += env.get_cost(*next_state)
            state = next_state
            nodes_expanded += 1
        if path[-1] == goal and cost < best_cost:
            best_path, best_cost = path, cost
    return {'path': best_path or [], 'cost': best_cost, 'nodes_expanded': nodes_expanded}
