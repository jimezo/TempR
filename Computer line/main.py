# http://acmp.ru/index.asp?main=task&id_task=57

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


if __name__ == '__main__':

    count_pig = input('Count pig: ')
    count_rouble_need = input('Count rouble for one LAN: ')
    count_rouble_have = input('Count rouble they have: ')
