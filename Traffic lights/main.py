
class Crossroad:

    def __init__(self, key):

        self.key = key

        self.next = None


class TraficLight:

    def __init__(self):

        self.crossroad = None

        self.count = 0


    def add_crossroad(self, key):

        crossroad = self.crossroad

        new_crossroad = Crossroad( key )

        if crossroad == None:

            self.crossroad = new_crossroad

            self.crossroad.next = TraficLight()

        else:

            self.crossroad.next.add_crossroad( key )


    def count_traficLight(self, count_trafic = 0):

        if self.crossroad != None:

            if self.crossroad.next != None:

                count_trafic = self.crossroad.next.count_traficLight( count_trafic + 1 )

        return count_trafic


    def Show_tunnels(self):

        if self.crossroad != None:

            print( self.crossroad.key )

            if ( self.crossroad.next != None ):

                self.crossroad.next.Show_tunnels()

        return


if __name__ == "__main__":

    trafic = TraficLight()

    count_crossroad = int( input("Enter count crossroad: \n\t> ") )

    for crossroad in range( count_crossroad ):

        trafic.add_crossroad( crossroad )

    print("Count trafic light: ", trafic.count_traficLight() - 1 )

    trafic.Show_tunnels()
