import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Function to find the vertex with minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def min_distance(self, dist, visited):
        min_dist = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v
        return min_index

    # Function to construct and print MST for a graph represented using adjacency matrix
    def dijkstra_mst(self):
        parent = [None] * self.V  # Array to store constructed MST
        dist = [sys.maxsize] * self.V  # Key values used to pick minimum weight edge in cut
        dist[0] = 0  # Make the source vertex key as 0 so that it is picked first
        visited = [False] * self.V  # To keep track of vertices included in MST

        parent[0] = -1  # First node is always the root of

        for _ in range(self.V):

            # Pick the minimum distance vertex from the set of vertices not yet processed.
            # u is always equal to src in the first iteration
            u = self.min_distance(dist, visited)

            # Put the minimum distance vertex in the shortest path tree
            visited[u] = True

            # Update dist value of the adjacent vertices of the picked vertex only if
            # the current distance is greater than new distance and the vertex is not in the MST
            for v in range(self.V):
                if self.graph[u][v] > 0 and not visited[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

# Take user input for the graph
V = int(input("Enter the number of vertices: "))
g = Graph(V)
print("Enter the adjacency matrix for the graph:")
for i in range(V):
    g.graph[i] = list(map(int, input().split()))

g.dijkstra_mst()

