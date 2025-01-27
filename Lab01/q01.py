import random

class system:
    def __init__(self):
        self.comps = {}

        for i in range(9):
            self.comps[chr(ord('a') + i)] = random.choice([0, 1])

class agent:
    def __init__(self):
        self.vurns = []
        

    def scan(self, i_comp):
        for key in i_comp:
            if i_comp[key] == 1:
                self.vurns.append(key)
        
    def patches(self, i_comp):
        for i in range(len(self.vurns)):
            i_comp[self.vurns[i]] == 1
            print(f'vurnebility at {self.vurns[i]} patched')
            patched = i_comp
        return patched
    
def run_agent(agent, system):
    percept = system.comps
    agent.scan(percept)
    system.comps = agent.patches(percept)


mysystem = system()
myagent = agent()
run_agent(myagent, mysystem)
