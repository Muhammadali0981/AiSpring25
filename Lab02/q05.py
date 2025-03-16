import random

class Hospital():
    def __init__(self):
        self.rooms = {f"Room {i}": None for i in range(1, 6)}
        self.medicines = {f"Room {i}": random.choice([True, False]) for i in range(1, 6)}
    
    def _display(self):
        for room, has_medicine in self.medicines.items():
            status = "Medicine Needed" if has_medicine else "No Delivery Required"
            print(f"{room}: {status}")

class Robot():
    def __init__(self):
        pass
    
    def _deliver(self, h):
        for room in h.medicines:
            if h.medicines[room]:
                print(f"Delivering medicine to {room}...")
                h.medicines[room] = False
            else:
                print(f"{room} does not need medicine.")

hospital = Hospital()
robot = Robot()
hospital._display()
robot._deliver(hospital)
hospital._display()