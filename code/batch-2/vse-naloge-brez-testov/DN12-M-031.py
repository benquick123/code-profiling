from itertools import cycle

def preberi(file_name):
    graph = {}
    with open(file_name) as node_connections:
        for node, adjacent_nodes in enumerate(node_connections, start = 1):
            graph[node] = [int(n) for n in adjacent_nodes.split()]
            while graph[node][0] != min(graph[node]):
                graph[node].append(graph[node].pop(0))
    return graph
            
def mozna_pot(path, graph):
    return (all(len(graph[n]) != 1 for n in path[1:-1])
            and len(graph[path[0]]) == len(graph[path[-1]]) == 1
            and all(node1 in graph[node0] for node0, node1 in zip(path, path[1:])))

def hamiltonova(path, graph):
    return (mozna_pot(path, graph) 
            and len(path) == 2 + len([n for n in graph if len(graph[n]) > 1])   
            and len(path) == len(set(path)))

def navodila(path, graph):
    turns = []
    for node0, node1, node2 in zip(path, path[1:], path[2:]):
        d = graph[node1].index(node2) - graph[node1].index(node0)
        turns.append(d if d >= 0 else d + len(graph[node1]))
    return turns

def prevozi(start, instructions, graph):
    nodes = [start, graph[start][0]]
    for exit0 in instructions:
        for exit1, exit_node in enumerate(cycle(graph[nodes[-1]]), 
                                          start = -graph[nodes[-1]].index(nodes[-2])):
            if exit1 == exit0:
                nodes.append(exit_node)
                break
    return nodes

def sosedi(nodes, graph):
    return {n1 for n0 in nodes for n1 in graph[n0]} - nodes
            
def razdalja(node0, node1, graph):
    distance = 0
    neighbours = {node0}
    while node1 not in neighbours:
        neighbours = sosedi(neighbours, graph)
        distance += 1
    return distance

def najkrajsa_navodila(node0, node1, graph):
    path = [node0]
    while path[-1] != node1:
        distances = {n: razdalja(n, node1, graph)
                    for n in graph[path[-1]]}
        path.append(min(distances, key = distances.get))
    return navodila(path, graph)
 

