# verkefni2



position = 1.1
pos_dir = ''


ir_str =  input('Direction: ')


    
def movement(position, ir_str):

    if ir_str == 'n' or ir_str == 'N':
        position += 1

    if ir_str == 's' or ir_str == 'S':
        position += -1

    if ir_str == 'a' or ir_str == 'A':
        position += 0.1

    if ir_str == 'v' or ir_str == 'V':
        position += -0.1
    return position


def positioning(position):
    if position == 1.1:
        pos_dir = '(N)orth.'
        if ir_str != 'n' or ir_str != 'N':
            print('Not a valid direction!')

    if position == 1.2:
        pos_dir = '(N)orth or (E)ast or (S)outh.'
        if ir_str == 'w' or ir_str == 'W':
            print('Not a valid direction!')

    if position == 1.3:
        pos_dir = '(S)outh or (E)ast.'
        if ir_str == 'w' or ir_str == 'n' or ir_str == 'W' or ir_str == 'N':
            print('Not a valid direction!')

    if position == 2.1:
        pos_dir = '(N)orth.'
        if ir_str != 'n' or ir_str != 'N':
            print('Not a valid direction!')

    if position == 2.2:
        pos_dir = '(W)est or (S)outh.'
        if ir_str == 'e' or ir_str == 'n' or ir_str == 'E' or ir_str == 'N':
            print('Not a valid direction!')

    if position == 2.3:
        pos_dir = '(W)est or (E)ast.'
        if ir_str == 's' or ir_str == 'n' or ir_str == 'S' or ir_str == 'N':
            print('Not a valid direction!')

    if position == 3.3:
        pos_dir = '(W)est or (S)outh.'
        if ir_str == 'e' or ir_str == 'n' or ir_str == 'E' or ir_str == 'N':
            print('Not a valid direction!')

    if position == 3.2:
        pos_dir = '(N)orth or (S)outh.'
        if ir_str == 'e' or ir_str == 'w' or ir_str == 'E' or ir_str == 'W':
            print('Not a valid direction!')

    if position == 3.1:
        pos_dir = 'Victory!'

    return pos_dir





    print('You can travel:', ) 

