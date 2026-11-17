"""
Experiment 2: A* (A-Star) Search Algorithm
Aim: Implement the A* search algorithm for pathfinding on a weighted graph.
"""

import heapq


def a_star(graph, heuristics, start, goal):
    """Finds the optimal path from start to goal using f(n) = g(n) + h(n)."""
    # Priority queue stores tuples: (f_score, g_score, current_node, path)
    open_list = [(heuristics[start], 0, start, [start])]
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')


if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # Heuristic values (estimated cost to reach 'D')
    heuristics = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

    path, total_cost = a_star(graph, heuristics, 'A', 'D')
    print(f"Optimal Path: {path}")
    print(f"Total Cost: {total_cost}")
