class Passenger:
    floor: int

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def floor_selection(self):
        floor = input('What floor does passenger ' + self.name + ' go to? ')
        self.floor = int(floor)
