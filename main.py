from Passenger import Passenger


def input_passenger():
    name = input('Input the passengers name: ')
    weight = input('Input the passengers weight: ')
    person = Passenger(name, float(weight))


def check_input(answer):
    if answer == 'Yes' or answer == 'No':
        return True
    return False


next_pas_check = True

while next_pas_check:
    input_passenger()
    check = input('Would you like to add more passengers? (Yes/No): ')
    if not check_input(check):
        print('Incorrect answer')
        continue
    if check == 'No':
        next_pas_check = False


def weight_count():
    pass


def floor_input():
    pass


# person = Passenger('Oleg', 14)
# print(person.name, person.weight)
