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


def dfs_agent(start, goal):
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph[node]): 
                stack.append((neighbor, path + [neighbor]))
    return None


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


def ucs_agent(start, goal):
    heap = [(0, start, [start])]
    visited = set()
    
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in weighted_graph[node]:
                heapq.heappush(heap, (cost + edge_cost, neighbor, path + [neighbor]))
    return None, float('inf')


print("DFS Agent:", dfs_agent('A', 'F'))
print("DLS Agent (limit 2):", dls_agent('A', 'F', 2))
print("DLS Agent (limit 3):", dls_agent('A', 'F', 3))
path, cost = ucs_agent('A', 'F')
print(f"UCS Agent: Path={path}, Cost={cost}")