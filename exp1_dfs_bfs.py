"""
Experiment 1: Depth First Search (DFS) & Breadth First Search (BFS)
Aim: Implement DFS and BFS algorithms on an undirected graph.
"""

from collections import deque

# Graph representation using Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs(graph, node, visited=None):
    """Recursive Depth First Search traversal."""
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    """Iterative Breadth First Search traversal using a Queue."""
    visited = set([start])
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == "__main__":
    print("DFS Traversal starting from A:")
    dfs(graph, 'A')

    print("\n\nBFS Traversal starting from A:")
    bfs(graph, 'A')
    print()
