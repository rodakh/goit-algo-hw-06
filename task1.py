import networkx as nx
import matplotlib.pyplot as plt

# Cтворимо граф соціальної мережі. Ми змоделюємо невелику мережу, де вузли представлятимуть людей, а ребра - зв'язки між ними (наприклад, дружбу).

G = nx.Graph()

G.add_nodes_from(range(1, 10))

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7), (5, 7), (6, 8), (7, 8), (8, 9)]
G.add_edges_from(edges)

nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()

# Аналіз графа
num_of_nodes = G.number_of_nodes()
num_of_edges = G.number_of_edges()
degrees = [G.degree(n) for n in G.nodes()]

print("Кількість вершин:", num_of_nodes)
print("Кількість ребер:", num_of_edges)
print("Ступені вершин:", degrees)

