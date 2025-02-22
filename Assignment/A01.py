import heapq
from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start], 0)])  # (Node, Path, Cost)
    visited = set()

    while queue:
        node, path, cost = queue.popleft()

        if node == goal:
            return path, cost  # Return path and correct total cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):  
                queue.append((neighbor, path + [neighbor], cost + weight))  # Accumulate cost

    return [], float("inf")

def ucs(graph, start, goal):
    pq = [(0, start, [start])]  # (Cost, Node, Path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost  # Return correct total cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return [], float("inf")

def greedy_best_first_search(graph, start, goal, heuristic):
    pq = [(heuristic[start], start, [start], 0)]  # (Heuristic, Node, Path, Cost)
    visited = set()

    while pq:
        _, node, path, cost = heapq.heappop(pq)

        if node == goal:
            return path, cost  # Return correct total cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor], cost + weight))

    return [], float("inf")

def iddfs(graph, start, goal, max_depth=10):
    def dls(node, goal, depth, path, cost):
        if depth == 0 and node == goal:
            return path, cost  # Return correct total cost
        if depth > 0:
            for neighbor, weight in graph.get(node, []):
                result = dls(neighbor, goal, depth - 1, path + [neighbor], cost + weight)
                if result:
                    return result
        return [], float("inf")

    for depth in range(max_depth):
        result, cost = dls(start, goal, depth, [start], 0)
        if result:
            return result, cost
    
    return [], float("inf")

# Define the graph and heuristic values
graph = {  
  "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],  
  "Zerind": [("Arad", 75), ("Oradea", 71)],  
  "Oradea": [("Zerind", 71), ("Sibiu", 151)],  
  "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],  
  "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],  
  "Rimnicu Vilcea": [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146)],  
  "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],  
  "Timisoara": [("Arad", 118), ("Lugoj", 111)],  
  "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],  
  "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],  
  "Drobeta": [("Mehadia", 75), ("Craiova", 120)],  
  "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],  
  "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],  
  "Giurgiu": [("Bucharest", 90)],  
  "Urziceni": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],  
  "Hirsova": [("Urziceni", 98), ("Eforie", 86)],  
  "Eforie": [("Hirsova", 86)],  
  "Vaslui": [("Urziceni", 142), ("Iasi", 92)],  
  "Iasi": [("Vaslui", 92), ("Neamt", 87)],  
  "Neamt": [("Iasi", 87)]  
}

heuristics = {
  "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242, "Eforie": 161,
  "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244,
  "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
  "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374
}

# Running all algorithms
results = []
start, goal = "Arad", "Hirsova"

bfs_result = bfs(graph, start, goal)
ucs_result = ucs(graph, start, goal)
gbfs_result = greedy_best_first_search(graph, start, goal, heuristics)
iddfs_result = iddfs(graph, start, goal)

results.append(("BFS", bfs_result))
results.append(("UCS", ucs_result))
results.append(("Greedy Best-First Search", gbfs_result))
results.append(("IDDFS", iddfs_result))

print(results)


