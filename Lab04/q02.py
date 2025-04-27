import heapq
import random
import time

class DynamicAStar:
    def __init__(self, graph, start, goal, heuristic):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.heuristic = heuristic
        self.costs = self.initialize_costs()
        self.last_update = time.time()
    
    def initialize_costs(self):
        """Initialize with base costs"""
        costs = {}
        for node in self.graph:
            costs[node] = {}
            for neighbor, base_cost in self.graph[node]:
                costs[node][neighbor] = base_cost
        return costs
    
    def update_costs(self):
        
        current_time = time.time()
        if current_time - self.last_update > 1.0:  # update every second
            for node in self.graph:
                for neighbor in self.graph[node]:
                    # Randomly adjust cost by ±20%
                    base_cost = self.graph[node][neighbor][1]
                    self.costs[node][neighbor] = max(1, int(base_cost * (0.8 + 0.4 * random.random())))
            self.last_update = current_time
    
    def find_path(self):
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        
        came_from = {}
        g_score = {node: float('inf') for node in self.graph}
        g_score[self.start] = 0
        
        f_score = {node: float('inf') for node in self.graph}
        f_score[self.start] = self.heuristic(self.start, self.goal)
        
        open_set_hash = {self.start}
        
        while open_set:
            current = heapq.heappop(open_set)[1]
            open_set_hash.remove(current)
            
            if current == self.goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                path.reverse()
                return path
            
            self.update_costs()  # check for cost updates
            
            for neighbor, _ in self.graph[current]:
                # Get the current dynamic cost
                current_cost = self.costs[current][neighbor]
                
                tentative_g_score = g_score[current] + current_cost
                
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.goal)
                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        open_set_hash.add(neighbor)
        
        return None  # No path found

# Example usage
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5), ('E', 12)],
    'C': [('F', 3), ('G', 4)],
    'D': [('H', 7)],
    'E': [('H', 3)],
    'F': [('H', 6)],
    'G': [('H', 5)],
    'H': []
}

def heuristic(node, goal):
   
    h_values = {'A': 10, 'B': 8, 'C': 6, 'D': 5, 'E': 4, 'F': 3, 'G': 2, 'H': 0}
    return h_values[node]

dyn_astar = DynamicAStar(graph, 'A', 'H', heuristic)
path = dyn_astar.find_path()
print("Dynamic A* path:", path)