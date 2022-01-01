class Passenger:
    Name: str
    Weight: float

    def __init__(self, name, weight):
        self.Name = name
        self.Weight = weight


def input_passenger():
    names = []
    weights = []
    person = Passenger(input('Input the passengers name: '), input('Input the passengers weight: '))
    names.append(person.Name)
    weights.append(person.Weight)
    return()


while True:
    input_passenger()
    print('Would you like to add more passengers? (Yes/No)')
    check = input()
    if check == 'Yes':
        continue
    elif check == 'No':
        break
    else:
        print('Incorrect answer')
        quit()


def weight_count():
    pass


def floor_input():
    pass


input_passenger()
weight_count()
floor_input()


# person = Passenger('Oleg', 14)
# print(person.Name, person.Weight)
