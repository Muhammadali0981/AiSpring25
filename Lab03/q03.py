from collections import deque
import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def dls_agent(start, goal, limit):
    return dls_recursive(start, goal, limit, [start], set())

def dls_recursive(node, goal, limit, path, visited):
    if node == goal:
        return path
    if limit <= 0:
        return None
    
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dls_recursive(neighbor, goal, limit-1, path + [neighbor], visited)
            if result is not None:
                return result
    return None

def iddfs(start, goal):
    depth = 0
    while True:
        result = dls_agent(start, goal, depth)
        if result is not None:
            return result
        depth += 1

# Bidirectional Search (using BFS from both ends)
def bidirectional_search(start, goal):
    if start == goal:
        return [start]
    
    # Forward search
    forward_queue = deque([(start, [start])])
    forward_visited = {start: [start]}
    
    # Backward search
    backward_queue = deque([(goal, [goal])])
    backward_visited = {goal: [goal]}
    
    while forward_queue and backward_queue:
        # Expand forward search
        f_node, f_path = forward_queue.popleft()
        for neighbor in graph[f_node]:
            if neighbor in backward_visited:
                return f_path + backward_visited[neighbor][::-1]
            if neighbor not in forward_visited:
                forward_visited[neighbor] = f_path + [neighbor]
                forward_queue.append((neighbor, f_path + [neighbor]))
        
        # Expand backward search
        b_node, b_path = backward_queue.popleft()
        for neighbor in graph[b_node]:
            if neighbor in forward_visited:
                return forward_visited[neighbor] + b_path[::-1]
            if neighbor not in backward_visited:
                backward_visited[neighbor] = b_path + [neighbor]
                backward_queue.append((neighbor, b_path + [neighbor]))
    
    return None

print("IDDFS:", iddfs('A', 'F'))
print("Bidirectional Search:", bidirectional_search('A', 'F'))