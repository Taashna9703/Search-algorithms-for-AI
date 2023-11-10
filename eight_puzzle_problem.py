import heapq
class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
    def total_cost(self):
        return self.cost + self.heuristic
    def __lt__(self, other):
        return self.total_cost() < other.total_cost()
    def __eq__(self, other):
        return self.state == other.state
def astar_search(start_state, goal_state, heuristic_func):
    open_list = []
    closed_list = set()
    start_node = Node(start_state)
    start_node.heuristic = heuristic_func(start_state, goal_state)
    heapq.heappush(open_list, start_node)
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == goal_state:
            return reconstruct_path(current_node)
        closed_list.add(current_node.state)
        for neighbor_state in get_neighbors(current_node.state):
            if neighbor_state in closed_list:
                continue
            neighbor_cost = current_node.cost + 1
            neighbor_heuristic = heuristic_func(neighbor_state, goal_state)
            neighbor_node = Node(neighbor_state, current_node, neighbor_cost,neighbor_heuristic)
            if not any(node == neighbor_node for node in open_list):
                heapq.heappush(open_list, neighbor_node)
    return None
def get_neighbors(state):
    empty_cell_index = state.index(0)
    possible_moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7],
    }
    neighbors = []
    for move in possible_moves[empty_cell_index]:
        neighbor_state = list(state)
        neighbor_state[empty_cell_index], neighbor_state[move] = neighbor_state[move], neighbor_state[empty_cell_index]
        neighbors.append(tuple(neighbor_state))
    return neighbors
def heuristic_func(state, goal_state):
    return sum(1 for a, b in zip(state, goal_state) if a != b)
def reconstruct_path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))
start_state = (7, 2, 6, 1, 0, 3, 8, 5, 4)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
path = astar_search(start_state, goal_state, heuristic_func)
print("\nPath:", path)
