import random

class system():
    def __init__(self, num):
        self.task = {}
        self.number = num

        for i in range(num):
            self.task[chr(ord('a') + i)] = random.choice(['failed', 'completed'])

    def _display(self):
        for i in range(self.number):
            print(f"task {chr(ord('a') + i)} status: {self.task[chr(ord('a') + i)]}")


class agent():
    def __init__(self):
        pass

    def _scan(s):
        for i in range(s.number):
            if s.task[chr(ord('a') + i)] == 'failed':
                print(f"retering task {chr(ord('a') + i)}")
                s.task[chr(ord('a') + i)] = 'completed'


myagent = agent()
sys = system(4)
sys._display()
agent._scan(sys)
sys._display()
