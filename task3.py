import networkx as nx
import random


G = nx.Graph()

# Додавання ребер з випадковими вагами
edges_with_weights = [
    (1, 2, random.randint(1, 10)), (1, 3, random.randint(1, 10)),
    (2, 4, random.randint(1, 10)), (2, 5, random.randint(1, 10)),
    (3, 6, random.randint(1, 10)), (4, 7, random.randint(1, 10)),
    (5, 7, random.randint(1, 10)), (6, 8, random.randint(1, 10)),
    (7, 8, random.randint(1, 10)), (8, 9, random.randint(1, 10))
]
G.add_weighted_edges_from(edges_with_weights)

# Використання вбудованої функції NetworkX для знаходження найкоротших шляхів
for node in G.nodes:
    print(f"Найкоротші шляхи від вершини {node}:")
    lengths = nx.single_source_dijkstra_path_length(G, node)
    for target_node, distance in lengths.items():
        print(f"  до вершини {target_node} = {distance}")
    print()
