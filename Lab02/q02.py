import random

class server:
    def __init__(self):
        self.tasks = random.choice([0, 6])
        self.load = self._load
    
    def _load(self):
        if self.tasks >= 4:
            return 'over'
        
        elif (self.tasks <= 3) and (self.tasks >= 2):
            return 'balance'

        elif (self.tasks <= 2):
            return 'under-balance'



class system:
    def __init__(self):
        self.servers = {}

        for i in range(0, 6):
            self.servers[chr(ord('a') + i)] = server()
    
class agent:
    def __init__(self, sy):
        self.s = system()

    def balancing(self):
        for i in self.s:
            if s[i].serves.load 