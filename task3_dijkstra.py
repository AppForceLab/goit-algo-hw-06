import networkx as nx
import pandas as pd
from task1_graph_analysis import G

# Завдання 3: Алгоритм Дейкстри

def dijkstra(graph, start):
    return nx.single_source_dijkstra_path_length(graph, start)

shortest_paths = {node: dijkstra(G, node) for node in G.nodes}

df_shortest_paths = pd.DataFrame(shortest_paths).fillna("-")
print("\nНайкоротші шляхи між всіма вершинами:")
print(df_shortest_paths)
