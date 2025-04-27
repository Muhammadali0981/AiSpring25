import heapq
from collections import defaultdict

def multi_goal_bfs(maze, start, goals):
    
    if not goals:
        return []
    
    goals = set(goals)
    visited_goals = set()
    path = [start]
    
    # Heuristic: Manhattan distance to nearest unvisited goal
    def heuristic(pos):
        if not goals - visited_goals:
            return 0
        return min(abs(pos[0]-g[0]) + abs(pos[1]-g[1]) for g in goals - visited_goals)
    
    current = start
    total_path = [start]
    
    while visited_goals != goals:
        # Standard BFS but with priority based on heuristic
        queue = []
        heapq.heappush(queue, (heuristic(current), current, [current]))
        visited = set()
        visited.add(current)
        found_path = None
        
        while queue:
            _, pos, path = heapq.heappop(queue)
            
            if pos in goals and pos not in visited_goals:
                visited_goals.add(pos)
                found_path = path
                current = pos
                break
            
            for neighbor in get_neighbors(maze, pos):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (heuristic(neighbor), neighbor, new_path))
        
        if found_path:
            total_path += found_path[1:]  # avoid duplicating the current node
        else:
            return None  # no path to remaining goals
    
    return total_path

def get_neighbors(maze, pos):
    
    rows, cols = len(maze), len(maze[0])
    x, y = pos
    neighbors = []
    
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != 1:
            neighbors.append((nx, ny))
    
    return neighbors

# Example usage
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goals = [(4, 4), (2, 2), (4, 0)]

path = multi_goal_bfs(maze, start, goals)
print("Multi-goal BFS path:", path)