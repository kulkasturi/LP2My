from collections import defaultdict
class Graph:
    def _init_(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                queue.extend(self.graph[vertex])

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

# Create graph from user input
g = Graph()
print("Enter edges (vertex1 vertex2), type 'done' when finished:")
while True:
    edge = input().strip()
    if edge.lower() == 'done':
        break
    u, v = edge.split()
    g.add_edge(u, v)

# Take input for starting vertex
start_vertex = input("Enter starting vertex for BFS and DFS: ").strip()

# Perform BFS and DFS
print("\nBFS starting from vertex", start_vertex, ":")
g.bfs(start_vertex)
print("\nDFS starting from vertex", start_vertex, ":")
g.dfs(start_vertex)