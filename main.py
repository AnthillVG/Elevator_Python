from Passenger import Passenger
from Elevator import Elevator

elevator = Elevator()


def new_passenger():
    person = Passenger(input("Input the passenger's name: "), float(input("Input the passenger's weight: ")))
    elevator.add_passenger(person)


def check_input(answer):
    if answer == 'yes' or answer == 'no':
        return True
    return False


def overload_check():
    if elevator.is_overloaded():
        print('The elevator is overloaded.')
        quit()


def elevator_passengers():
    next_pas_check = True
    while next_pas_check:
        new_passenger()
        check = input('Would you like to add a passenger? (Yes/No): ').lower()
        if not check_input(check):
            while not check_input(check):
                check = input('Incorrect answer. Please, try again. (Yes/No): ')
        if check == 'no':
            next_pas_check = False


def floor_print():
    floor_list = elevator.elevator_moving()
    for floor in floor_list:
        left_passengers_list = ''
        for passenger in floor_list[floor]:
            left_passengers_list += passenger.name + ', '
        print('On floor ' + str(floor) + ' left: ' + left_passengers_list.strip(', '))


elevator_passengers()
overload_check()
elevator.floor_selection()
floor_print()
