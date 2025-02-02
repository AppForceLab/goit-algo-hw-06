import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Завдання 1: Створення та аналіз графа
G = nx.Graph()

# Визначаємо вершини
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
G.add_nodes_from(nodes)

# Визначаємо ребра з вагами
edges = [
    ("A", "B", 5), ("A", "C", 10), ("B", "D", 3),
    ("C", "D", 4), ("C", "E", 8), ("D", "F", 6),
    ("E", "F", 2), ("E", "G", 7), ("F", "H", 9),
    ("G", "I", 3), ("H", "J", 4), ("I", "J", 5),
    ("B", "E", 12), ("D", "G", 11)
]
G.add_weighted_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

df = pd.DataFrame(list(degrees.items()), columns=["Вершина", "Ступінь"])
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(df)
