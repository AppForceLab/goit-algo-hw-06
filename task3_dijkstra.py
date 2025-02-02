import heapq
import networkx as nx
import pandas as pd
from task1_graph_analysis import G

# Завдання 3: Алгоритм Дейкстри

def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > shortest_paths[current_node]:
            continue
        
        for neighbor, attributes in graph[current_node].items():
            distance = current_distance + attributes['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

shortest_paths = {node: dijkstra(G, node) for node in G.nodes}

df_shortest_paths = pd.DataFrame(shortest_paths).fillna("-")
print("\nНайкоротші шляхи між всіма вершинами:")
print(df_shortest_paths)