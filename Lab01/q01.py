import random

class system:
    def __init__(self):
        self.comps = {}

        for i in range(9):
            self.comps[chr(ord('a') + i)] = random.choice([0, 1])

class agent:
    def __init__(self, i_comp):
        self.agent_comp = i_comp
        self.vurns = []
    
    def scan(self):
        for key in self.agent_comp:
            if self.agent_comp[key] == 1:
                self.vurns.append(key)
        
    def patches(self):
        for i in range(len(self.vurns)):
            self.agent_comp[self.vurns[i]] == 1
            print(f'vurniblity at {self.vurns[i]} patched')
        

mysystem = system()
myagent = agent(mysystem.comps)
myagent.patches()
