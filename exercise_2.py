'''Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі,
який було розроблено у першому завданні.

Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в
отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.'''

import networkx as nx
from collections import deque

def dfs(gr, start, stop, visited=None, path=None):
    if visited == None:
        visited = {start}
    # saving path for node
    if path == None:
        path = [start]
    
    if start == stop:
        return path

    for neighbor in gr.neighbors(start):
            if neighbor not in visited:
                visited.add(neighbor)
                # add new path for new node
                new_path = dfs(gr, neighbor, stop, visited, path + [neighbor])

                if new_path is not None:
                    return new_path
    return None


def bfs(gr, start, stop):
    # saving path
    search_queue = deque([(start, [start])])
    visited = {start}

    while search_queue:
        node, path = search_queue.popleft()
        
        if node == stop:
            return path
        
        for neighbor in gr.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                # add new path for new node
                search_queue.append((neighbor, path + [neighbor]))
    
    return None


# Creating
my_graph = nx.Graph()
my_graph.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'G'])
my_graph.add_edges_from([('A', 'B'), ('A', 'C'), ('C', 'B'), ('G', 'D'), ('C', 'E'), ('E', 'D'), ('G', 'E')])

print(dfs(my_graph, 'A', 'G'))
print(bfs(my_graph, 'A', 'G'))
