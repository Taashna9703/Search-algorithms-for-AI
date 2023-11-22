from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, v, w):
        self.adj_list[v].append(w)

    def dfs_helper(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for n in self.adj_list[v]:
            if not visited[n]:
                self.dfs_helper(n, visited)

    def dfs(self, v):
        visited = [False] * self.vertices
        self.dfs_helper(v, visited)

def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 4)

    print("Depth First Traversal for the given graph (starting from vertex 0) is:")
    g.dfs(0)

if __name__ == "__main__":
    main()

