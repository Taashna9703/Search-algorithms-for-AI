from collections import deque
def water_jug_problem(jug1_C, jug2_c, target):
    def get_neighbors(state):
        a, b = state
        return {(jug1_C, b), (a, jug2_c), (0, b), (a, 0),
                (min(a+b, jug1_C), 0 if a+b < jug1_C else b-(jug1_C-a)),
                (0 if a+b < jug2_c else a-(jug2_c-b), min(a+b, jug2_c))}
    start_state=(0,0)
    queue=deque([(start_state,[])])
    visited=set()
    while queue:
        state, path=queue.popleft()
        if state[0]==target or state[1]==target:
            return path+[state]
        visited.add(state)
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                queue.append((neighbor,path+[state]))
    return None
jug1_C=4
jug2_c=3
target=2
print(water_jug_problem(jug1_C, jug2_c, target))
    