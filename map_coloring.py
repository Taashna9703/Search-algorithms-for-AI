def is_safe(graph, node, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def color_map(graph, colors, assignment, nodes):
    if not nodes:
        return assignment
    node = nodes.pop()
    for color in colors:
        if is_safe(graph, node, color, assignment):
            assignment[node] = color
            result = color_map(graph, colors, assignment, nodes)
            if result is not None:
                return result
            assignment.pop(node)
    nodes.append(node)  # Backtrack
    return None
def map_coloring(graph, colors):
    assignment = {}
    nodes = list(graph.keys())
    result = color_map(graph, colors, assignment, nodes)
    return result
if __name__ == "__main__":
    graph = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
    }
    colors = ['Red', 'Green', 'Blue']
    solution = map_coloring(graph, colors)
    if solution is not None:
        print("Map coloring solution:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution exists.")
