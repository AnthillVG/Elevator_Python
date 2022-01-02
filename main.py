from Passenger import Passenger


passenger_names = []
passenger_weights = []
floors = []


def input_passenger():
    Passenger.name = input('Input the passengers name: ')
    Passenger.weight = input('Input the passengers weight: ')
    # person = Passenger(name, float(weight))
    passenger_names.append(Passenger.name)
    passenger_weights.append(Passenger.weight)


def check_input(answer):
    if answer == 'yes' or answer == 'no':
        return True
    return False


next_pas_check = True
while next_pas_check:
    input_passenger()
    check = input('Would you like to add a passenger? (Yes/No): ')
    check = check.lower()
    if not check_input(check):
        while not check_input(check):
            check = input('Incorrect answer. Please, try again: ')
    if check == 'no':
        next_pas_check = False


def weight_count():
    for i in range(0, len(passenger_weights)):
        pass


def floor_input():
    for i in range(0, len(passenger_names)):
        floor = input('What floor does passenger ' + passenger_names[i] + ' go to? ')
        floors.append(floor)


floor_input()
print(passenger_names)
print(passenger_weights)
print(floors)


# person = Passenger('Oleg', 14)
# print(person.name, person.weight)
