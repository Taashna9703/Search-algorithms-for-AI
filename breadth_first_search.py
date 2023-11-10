from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, v, w):
        self.adj_list[v].append(w)

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque()
        visited[start] = True
        queue.append(start)
        while queue:
            i = queue.popleft()
            print(i, end=" ")
            for n in self.adj_list[i]:
                if not visited[n]:
                    visited[n] = True
                    queue.append(n)
def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    print("Breadth-First Traversal for the given graph (starting from vertex 0):")
    g.bfs(0)
if __name__ == "__main__":
    main()
