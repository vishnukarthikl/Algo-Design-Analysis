from copy import deepcopy
import random


class Graph:
    def __init__(self):
        self.connections = {}

    def add_connections(self, node_index, connected_nodes):
        self.connections[int(node_index)] = map(lambda x: int(x), connected_nodes)

    def find_min_cut(self):
        connections = deepcopy(self.connections)
        while (len(connections) > 2):
            connections = self.contract(connections)
        return len(connections[connections.keys()[0]])

    def contract(self, connections):
        u, v = self.pick_random_edge(connections)
        nodes_connected_to_u = connections[u]
        for nodes_connected_to_v in connections[v]:
            nodes_connected_to_u.append(nodes_connected_to_v)
        connections[u] = filter(lambda x: x != u and x != v, connections[u])
        del (connections[v])
        self.rename(connections, v, u)
        return connections


    def pick_random_edge(self, connections):
        first_vertex = random.sample(connections, 1)[0]
        second_vertex = random.sample(connections[first_vertex], 1)[0]
        return first_vertex, second_vertex

    def rename(self, connections, old_node, merged_node):
        for node in connections:
            for i in range(len(connections[node])):
                if connections[node][i] == old_node:
                    connections[node][i] = merged_node


graph = Graph()
contents = file.read(file('kargerMinCut.txt'))
connections = contents.split('\r\n')
for connection in connections[:-1]:
    connection_split = connection.split('\t')
    vertex_index = connection_split[0]
    graph.add_connections(vertex_index, connection_split[1:-1])

min = float('inf')
for _ in range(200):
    cuts = graph.find_min_cut()
    if cuts < min:
        min = cuts

print min
