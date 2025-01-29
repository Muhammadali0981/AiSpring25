import random

class system:
    def __init__(self):
        self.comps = {}

        for i in range(9):
            self.comps[chr(ord('a') + i)] = random.choice([0, 1])
    
    def final_check(self):
        f = 0
        for key in self.comps:
            if self.comps[key] == 1:
                print(f"vulnerabilities still present at {key}")
                f += 1
        if f == 0:
            print("no vulnerabilities found")
                

class agent:
    def __init__(self):
        self.vurns = []
        

    def scan(self, i_comp):
        for key in i_comp:
            if i_comp[key] == 1:
                self.vurns.append(key)
        
    def patches(self, i_comp):
        for i in range(len(self.vurns)):
            i_comp[self.vurns[i]] = 0
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
mysystem.final_check()
