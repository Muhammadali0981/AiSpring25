class Building():
    def __init__(self):
        self.rooms = {
            'a': 'Safe', 'b': 'Safe', 'c': 'Fire',
            'd': 'Safe', 'e': 'Fire', 'f': 'Safe',
            'g': 'Safe', 'h': 'Safe', 'j': 'Fire'
        }
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
    
    def _display(self):
        for room, status in self.rooms.items():
            symbol = "🔥" if status == "Fire" else " "
            print(f"Room {room}: {symbol}")

class FireRobot():
    def __init__(self):
        pass
    
    def _extinguish(self, b):
        for room in b.path:
            if b.rooms[room] == 'Fire':
                print(f"Fire detected in Room {room}. Extinguishing...")
                b.rooms[room] = 'Safe'
            else:
                print(f"Room {room} is safe. Moving on...")

building = Building()
robot = FireRobot()
building._display()
robot._extinguish(building)
building._display()