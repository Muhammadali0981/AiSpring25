import random

class server:
    def __init__(self):
        self.tasks = random.choice(range(0, 5))
        self.load = self._load()
    
    def _load(self):
        if self.tasks >= 4:
            return 'over'
        
        elif (self.tasks <= 3) and (self.tasks >= 2):
            return 'balance'

        elif (self.tasks < 2):
            return 'under'



class system:
    def __init__(self):
        self.servers = {}

        for i in range(0, 6):
            self.servers[chr(ord('a') + i)] = server()
    
    def _display(self):
        for i in self.servers:
            print(f'Server {i} tasks: {self.servers[i].tasks} load: {self.servers[i].load} ')



class agent:
    def __init__(self, sys):
        self.s = sys
        self._over = []
        self._under = []

    def balancing(self):
        for i in self.s.servers:
            if self.s.servers[i].load == 'over':
                self._over.append(i)
            elif self.s.servers[i].load == 'under':
                self._under.append(i)
    
        for i in self._over:
            self.s.servers[i].tasks -= 1
            self.s.servers[i].load = 'balance'
        for i in self._under:
            self.s.servers[i].tasks += 1
            self.s.servers[i].load = 'balance'
        
        print(f'all servers balanced')
        self.s._display()


mysystem = system()
mysystem._display()
myagent = agent(mysystem)
myagent.balancing()