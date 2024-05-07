def kruskal_minimum_spanning_tree(graph):
    def find_parent(parents, node):
        if parents[node] == node:
            return node
        return find_parent(parents, parents[node])

    def union(parents, rank, node1, node2):
        root1 = find_parent(parents, node1)
        root2 = find_parent(parents, node2)
        if rank[root1] < rank[root2]:
            parents[root1] = root2
        elif rank[root1] > rank[root2]:
            parents[root2] = root1
        else:
            parents[root1] = root2
            rank[root2] += 1

    minimum_spanning_tree = []
    edges = []
    num_nodes = len(graph)
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))
    edges.sort()  # Sort edges by weight
    parents = {node: node for node in range(num_nodes)}
    rank = {node: 0 for node in range(num_nodes)}

    for edge in edges:
        weight, node1, node2 = edge
        root1 = find_parent(parents, node1)
        root2 = find_parent(parents, node2)
        if root1 != root2:
            minimum_spanning_tree.append((node1, node2, weight))
            union(parents, rank, root1, root2)
    return minimum_spanning_tree

def create_graph():
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    print("Enter the adjacency matrix (space-separated elements):")
    graph = []
    for _ in range(num_nodes):
        row = list(map(int, input().split()))
        graph.append(row)
    return graph

user_graph = create_graph()
result = kruskal_minimum_spanning_tree(user_graph)
print("Minimum Spanning Tree:")
for edge in result:
    print(edge)

