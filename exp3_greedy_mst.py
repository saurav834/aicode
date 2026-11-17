"""
Experiment 3: Greedy Search Algorithm (Prim's Minimum Spanning Tree)
Aim: Implement a Greedy Search algorithm to find the Minimum Spanning Tree (MST).
"""

import heapq


def prim_mst(graph, start):
    """Finds the Minimum Spanning Tree using Prim's Greedy Algorithm."""
    mst = []
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)
    total_cost = 0

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            total_cost += cost
            for next_to, next_cost in graph[to].items():
                if next_to not in visited:
                    heapq.heappush(edges, (next_cost, to, next_to))

    return mst, total_cost


if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 4},
        'C': {'A': 3, 'B': 1, 'D': 5},
        'D': {'B': 4, 'C': 5}
    }

    mst_edges, cost = prim_mst(graph, 'A')
    print("Edges in Minimum Spanning Tree:", mst_edges)
    print("Total MST Cost:", cost)
