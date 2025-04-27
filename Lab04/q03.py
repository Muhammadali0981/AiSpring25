from collections import deque
import heapq

class DeliveryScheduler:
    def __init__(self, locations, time_windows, distance_matrix):
        self.locations = locations  # list of location names
        self.time_windows = time_windows  # dict: {location: (open, close)}
        self.distance_matrix = distance_matrix  # 2D array of distances
        self.location_index = {loc: idx for idx, loc in enumerate(locations)}
    
    def time_window_heuristic(self, current_loc, unvisited):
        """Heuristic that considers both distance and urgency of time windows"""
        if not unvisited:
            return 0
        
        min_heuristic = float('inf')
        current_time = self.current_time
        current_idx = self.location_index[current_loc]
        
        for loc in unvisited:
            idx = self.location_index[loc]
            distance = self.distance_matrix[current_idx][idx]
            time_left = self.time_windows[loc][1] - current_time
            urgency = max(0, (time_left - distance) / (time_left + 1e-6))  # normalize
            
            # Combine distance and urgency (lower is better)
            heuristic = distance * (1 + urgency * 2)  # urgency has more weight
            min_heuristic = min(min_heuristic, heuristic)
        
        return min_heuristic
    
    def schedule_deliveries(self, start_location, start_time=0):
        unvisited = set(self.locations)
        unvisited.remove(start_location)
        
        self.current_time = start_time
        current_loc = start_location
        path = [current_loc]
        total_distance = 0
        
        while unvisited:
            # Use priority queue based on heuristic
            queue = []
            current_idx = self.location_index[current_loc]
            
            for loc in unvisited:
                idx = self.location_index[loc]
                distance = self.distance_matrix[current_idx][idx]
                arrival_time = self.current_time + distance
                
                # Skip if we can't make it before the window closes
                if arrival_time > self.time_windows[loc][1]:
                    continue
                
                heuristic_val = self.time_window_heuristic(loc, unvisited - {loc})
                heapq.heappush(queue, (heuristic_val, loc, distance))
            
            if not queue:
                return None  # no valid path
            
            _, next_loc, distance = heapq.heappop(queue)
            path.append(next_loc)
            total_distance += distance
            self.current_time += distance
            unvisited.remove(next_loc)
            current_loc = next_loc
        
        return path, total_distance

# Example usage
locations = ['Depot', 'A', 'B', 'C', 'D']
time_windows = {
    'Depot': (0, 100),
    'A': (2, 10),
    'B': (5, 15),
    'C': (10, 20),
    'D': (15, 30)
}

distance_matrix = [
    [0, 5, 8, 6, 7],  # Depot
    [5, 0, 3, 4, 2],   # A
    [8, 3, 0, 2, 5],    # B
    [6, 4, 2, 0, 3],    # C
    [7, 2, 5, 3, 0]     # D
]

scheduler = DeliveryScheduler(locations, time_windows, distance_matrix)
path, total_distance = scheduler.schedule_deliveries('Depot')
print("Delivery route:", path)
print("Total distance:", total_distance)