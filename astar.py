import heapq
class Node():
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state=state
        self.parent=parent
        self.cost=cost
        self.heuristic=heuristic
    def total_cost(self):
        totalcost=self.heuristic+self.cost
        return totalcost
def astar(start, goal):
        open=[]
        closed=set()
        startnode=Node(start)
        startnode.heuristic=heuristicf(start, goal)
        heapq.heappush(open, startnode)
        while open:
            current=heapq.heappop(open)
            if current == goal:
                return reconstruct_path(current)
            closed.add(current)
            for neighbor in get_neighbors(current.state):
                if neighbor in closed:
                    continue
                neighborcost=current.cost+1
                neighborheuristic=heuristicf(neighbor, goal)
                neighbornode=Node(neighbor, current, neighborcost, neighborheuristic)
                if not any(node == neighbornode for node in open):
                    heapq.heappush(open, neighbornode)
            return None
def get_neighbors(state):
        x,y=state
        neighbors=[(x+1, y),(x,y+1),(x-1,y),(x, y-1)]
        return neighbors

def heuristicf(state, goal):
        x, y=goal
        dx, dy= goal
        return abs(dx-x)+abs(dy-y)
def reconstruct_path(node):
    
        path = []
        while node is not None:
            path.append(node.state)
            node = node.parent
        return list(reversed(path))

# Example usage:
start_state = (0, 0) 
goal_state = (5, 5)   
path = astar(start_state, goal_state)
print("Path:", path)
