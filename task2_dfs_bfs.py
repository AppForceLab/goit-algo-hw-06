import networkx as nx
from task1_graph_analysis import G

# Завдання 2: Реалізація алгоритмів DFS та BFS

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print("\nDFS шлях:")
dfs(G, "A")


def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph.neighbors(vertex)) - visited)

print("\nBFS шлях:")
bfs(G, "A")
