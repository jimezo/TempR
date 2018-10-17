# http://acmp.ru/index.asp?main=task&id_task=57

from math import fabs
import re

# Function for check validation value (N) - count pig
def N_isvalid(N):

    if ( str(N).isdigit() ):

        if ( int(N) >= 1 and int(N) <= 10**3 ):
            return True

    return False


# Function for check validation value (c) - how many rouble them need
def rouble_need(c):

    if ( str(c).isdigit() ):

        if ( int(c) >= 0 and int(c) <= 10**4 ):
            return True

    return False


# Function for check validation value (p) - how many rouble they have
def rouble_have(p):

    if ( str(p).isdigit() ):

        if ( int(p) >= 0 and int(p) <= 10**15 ):
            return True

    return False


# Function for check validation coordinates
def coordinates_isvalid(coordinates):

    coordinates = re.match('\d+', coordinates)

    print(coordinates)
    if ( int(coordinates) >= -1000 and int(coordinates) <= 1000 ):
        return True

    return False


if __name__ == '__main__':

    count_pig = 0
    count_rouble_need = 0
    count_rouble_have = 0

    pig_coordinates = []

    provider_coordinate = []

    print('Settings: \n')

    while 1:

        count_pig = input('\tCount pig: ')
        if ( N_isvalid(count_pig) ):
            break

    while 1:

        count_rouble_need = input('\tCount rouble for one LAN: ')
        if ( rouble_need(count_rouble_need) ):
            break

    while 1:

        count_rouble_have = input('\tCount rouble they have: ')
        if ( rouble_have(count_rouble_have) ):
            break


    print('\nEnter "x" and "y" coordinates, where "x" and "y" <= 1000 by module \n')

    print('Provider coordinate\n')

    while 1:

        x = input('\tEnter "x" coordinate: ')
        if coordinates_isvalid(x):

            y = input('\tEnter "y" coordinate: ')
            if coordinates_isvalid(y):

                provider_coordinate.append([x, y])
                break


    for pig in range( int(count_pig) ):

        error = False

        print('Pig village №' + str(pig + 1) )

        while 1:


            if error:
                print('\n\tEnter "x" and "y" coordinates all pigs, where "x" and "y" <= 1000 by module \n')
                error = False

            x = input('\tEnter "x" coordinate: ')
            if coordinates_isvalid(x):

                y = input('\tEnter "y" coordinate: ')
                if coordinates_isvalid(y):

                    pig_coordinates.append([x,y])
                    break

            error = True

    tugrics = 0
    for pig in pig_coordinates:

        tugrics += (provider_coordinate[0] + pig[0]) + (provider_coordinate[1] + pig[1])

    print(tugrics)
