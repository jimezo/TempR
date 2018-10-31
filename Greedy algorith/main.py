
class GreedyAlgorith:

    def __init__(self, size = 0):

        self.size = size

        self.matrix = []

        self.min_values = []


    def set_matrix(self):

        for cols in range( self.size ):

            row = []

            for rows in range( self.size ):

                if cols == rows:

                    row.append(0)

                    continue

                value = int( input("Enter value for ["+ str(cols) +"][" + str(rows) +"]: \t\n > ") )

                row.append( value )

            self.matrix.append( row )


    def get_min(self):

        for cols in range( self.size ):

            min = max( self.matrix[cols] )

            for rows in range( self.size ):

                if cols == rows:

                    continue

                if self.matrix[cols][rows] < min:

                    min = self.matrix[cols][rows]

            self.min_values.append( min )

        return self.min_values


    def show_matrix(self):

        print ( self.matrix )


if __name__ == "__main__":

    matrix = GreedyAlgorith(3)

    matrix.set_matrix()

    matrix.show_matrix()

    min_values = matrix.get_min()

    print("Min values: ", min_values )
