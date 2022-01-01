def input_passenger():
    pas_name = input('Input the passengers name: ')
    pas_weight = input('Input the passengers weight: ')
    return()


while 1:
    input_passenger()
    print('Would you like to add more passengers? (Yes/No)')
    check = input()
    if check == 'No':
        break
    elif check == 'Yes':
        continue
    else:
        print('Incorrect answer')
        quit()