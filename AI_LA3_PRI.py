import heapq

def greedy_prim(graph):
    minimum_spanning_tree = []
    visited = set()
    start_node = list(graph.keys())[0]
    priority_queue = [(0, start_node, None)]
    
    while priority_queue:
        weight, current_node, parent = heapq.heappop(priority_queue)
        if current_node not in visited:
            visited.add(current_node)
            minimum_spanning_tree.append((parent, current_node, weight))
            for neighbor, edge_weight in graph[current_node].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (edge_weight, neighbor, current_node))
    
    return minimum_spanning_tree

def create_graph():
    graph = {}
    edges = input("Enter edges and their weights in the format 'node1 node2 weight', separate each edge by space (or 'done' to finish):\n")
    while edges != "done":
        node1, node2, weight = edges.split()
        weight = int(weight)
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = weight
        graph[node2][node1] = weight
        edges = input()
    return graph

graph = create_graph()
result = greedy_prim(graph)

print("Minimum Spanning Tree:")
for edge in result:
    print(edge)

