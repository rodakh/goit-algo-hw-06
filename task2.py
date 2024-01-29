import networkx as nx


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited


G = nx.Graph()
G.add_nodes_from(range(1, 10))
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7), (5, 7), (6, 8), (7, 8), (8, 9)]
G.add_edges_from(edges)

# Виконання DFS та BFS
dfs_result = dfs(G, 1)
bfs_result = bfs(G, 1)

print("DFS:", dfs_result)
print("BFS:", bfs_result)

# Порівняння результатів
# DFS дає результати, які показують, як можна досягти кожного вузла, використовуючи глибинний прохід.
# BFS дає результати, які показують, як можна досягти кожного вузла, використовуючи ширинний прохід.
# Різниця в результатах пояснюється різними підходами до обходу графа: DFS "занурюється" в глибину графа, тоді як BFS рухається по рівнях.

# Висновки:
# - DFS є корисним для завдань, де потрібно дослідити всі можливі шляхи або знайти рішення, не обов'язково найкоротше.
# - BFS краще підходить для пошуку найкоротших шляхів або для аналізу рівнів відносин в графі.