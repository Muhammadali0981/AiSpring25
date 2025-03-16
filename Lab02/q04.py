import random

class System():
    def __init__(self):
        self.components = {}
        self.vulnerability_levels = ['Safe', 'Low Risk Vulnerable', 'High Risk Vulnerable']
        for i in range(9):
            self.components[chr(ord('A') + i)] = random.choice(self.vulnerability_levels)
    
    def _display(self):
        for i in range(9):
            print(f"Component {chr(ord('A') + i)} status: {self.components[chr(ord('A') + i)]}")

class Agent():
    def __init__(self):
        pass
    
    def _scan(self, s):
        for i in range(9):
            if s.components[chr(ord('A') + i)] == 'Safe':
                print(f"Component {chr(ord('A') + i)} is secure.")
            elif s.components[chr(ord('A') + i)] == 'Low Risk Vulnerable':
                print(f"Warning: Component {chr(ord('A') + i)} is Low Risk Vulnerable. Patching...")
                s.components[chr(ord('A') + i)] = 'Safe'
            else:
                print(f"Alert: Component {chr(ord('A') + i)} is High Risk Vulnerable. Premium service required.")

sys = System()
agent = Agent()
sys._display()
agent._scan(sys)
sys._display()