import heapq
class PuzzleNode:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.manhattan_distance = self.calculate_manhattan_distance()
    def calculate_manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                num = self.state[i][j]
                if num != 0:
                    x_goal = (num - 1) // 3
                    y_goal = (num - 1) % 3
                    distance += abs(x_goal - i) + abs(y_goal - j)
        return distance
    def total_cost(self):
        return self.depth + self.manhattan_distance
    def __lt__(self, other):
        return self.total_cost() < other.total_cost()
    def __eq__(self, other):
        return self.state == other.state
def get_neighbors(state):
    neighbors = []
    x, y = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors
def astar_search(start_state, goal_state):
    open_list = []
    closed_set = set()
    start_node = PuzzleNode(start_state)
    heapq.heappush(open_list, start_node)
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == goal_state:
            return reconstruct_path(current_node)
        closed_set.add(tuple(map(tuple, current_node.state)))
        for neighbor_state in get_neighbors(current_node.state):
            neighbor_node = PuzzleNode(neighbor_state, current_node, current_node.depth + 1)

            if tuple(map(tuple, neighbor_state)) in closed_set:
                continue
            if not any(node == neighbor_node for node in open_list):
                heapq.heappush(open_list, neighbor_node)
    return None
def reconstruct_path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))
def print_puzzle(puzzle):
    for row in puzzle:
        print(row)
    print()
# Example usage:
start_state = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
path = astar_search(start_state, goal_state)
if path:
    for step, state in enumerate(path):
        print(f"Step {step + 1}:")
        print_puzzle(state)
else:
    print("No solution found.")
