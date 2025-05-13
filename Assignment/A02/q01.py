def find_peak(N, query):
  
    current = 0
    while True:
        left = current - 1 if current > 0 else None
        right = current + 1 if current < N else None
        curr_val = query(current)
        left_val = query(left) if left is not None else float('-inf')
        right_val = query(right) if right is not None else float('-inf')

       
        if curr_val >= left_val and curr_val >= right_val:
            return current
        
        elif right_val > curr_val:
            current = right
        else:
            current = left

def query(x):
    return -1 * (x - 7)**2 + 49


