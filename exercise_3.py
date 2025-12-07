'''Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі:
додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.'''

import networkx as nx


def dijkstra(graph: nx.Graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    parents = {node: None for node in graph.nodes}
    unvisited = list(graph.nodes)
    visited = []

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])

        if distances[current_node] == float('inf'):
            break

        for curr, neighbor, weight in graph.edges(current_node, data=True):
            distance = distances[current_node] + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node

        visited.append(current_node)
        unvisited.remove(current_node)

    return distances, parents

def short(fr, to):
    distance, parent = dijkstra(my_graph, fr)
    way = []
    
    if distance[to] == float('inf'):
        return None
    
    curr = to
    while curr is not None:
        way.append(curr)
        curr = parent[curr]

    way.reverse()

    return f'Short weight: {distance[to]}\n{' --> '.join(way)}'

# Creating
my_graph = nx.Graph()
my_graph.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'G'])
my_graph.add_edge('A', 'B', weight=2)
my_graph.add_edge('A', 'C', weight=10)
my_graph.add_edge('C', 'B', weight=2)
my_graph.add_edge('G', 'D', weight=10)
my_graph.add_edge('C', 'E', weight=5)
my_graph.add_edge('E', 'D', weight=1)
my_graph.add_edge('G', 'E', weight=1)


#here we set searching to node
print(short('A', 'G'))
