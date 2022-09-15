class Bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        if not self.avail_seats():
            return False

        self.passengers.append(name)
        return True

    def avail_seats(self):
        return self.capacity - len(self.passengers)


bus = Bus(3)
names = ["tina", "claire", "mika", "cena", "zawa"]
names.sort()

for x in names:
    sucess = bus.add_passengers(x)

    if sucess:
        print(f"Added {x} to bus sucessfully!")

    else:
        print(f"No avail seats for {x} !")


