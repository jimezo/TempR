# http://acmp.ru/index.asp?main=task&id_task=15



class Way:

    def __init__(self, count_city = 0):

        if ( count_city < 0 and count_city > 100 ):

            return False

        self.count_city = count_city

        self.city = [ [0, 1, 0, 0, 0],
                      [1, 0, 1, 1, 0],
                      [0, 1, 0, 0, 0],
                      [0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0]]

    def set_city(self):

        self.city.clear()

        for rows in range( self.count_city ):

            ways = []

            for cols in range( self.count_city ):

                if rows == cols:

                    ways.append( 0 )

                    continue

                while True:

                    value = int(input( "Enter 1 or 0 for [" + str( rows + 1 ) + ', ' + str( cols + 1 ) + '] \n\t > '))


                    if value < 0 or value > 1:

                        continue

                    break

                ways.append( value )

            self.city.append( ways )


    def count_way(self):

        ways = []

        for rows in range(len( self.city )):

            for cols in range(len( self.city[rows] )):

                if (self.city[rows][cols] == 1 ):

                    if ( [cols + 1, rows + 1] not in ways):

                        ways.append( [rows + 1, cols + 1] )

        print( ways )

        return len(ways)


if __name__ == "__main__":

    way = Way(5)

    way.set_city()

    print( way.count_way() )
