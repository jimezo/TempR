class GreedyAlgorith:

    # Function contractor
    def __init__(self, size = 0):

        self.size = size # Variable there save matrix size

        self.matrix = [] # List there save matrix

        self.min_values = {}

        self.optimal_way = {}


    def set_matrix(self):

        for cols in range( self.size ):

            row = []

            for rows in range( self.size ):

                # Cols and rows not can cross yorself, so, add 0 to matrix and pass next value
                if cols == rows:

                    row.append(0)

                    continue

                value = int( input("Enter value for ["+ str(cols) +"][" + str(rows) +"]: \t\n > ") )

                row.append( value )

            self.matrix.append( row )


    # This function find minimal value from matrix and return dict with minimal value
    def get_min(self):

        for cols in range( self.size ):

            # Assign only one rows from matrix to variable min
            min = max( self.matrix[cols] )

            for rows in range( self.size ):

                if cols == rows:

                    continue

                if self.matrix[cols][rows] < min:

                    min = self.matrix[cols][rows]

                if rows + 1 == size:

                    # Save minimal value and him coordinates(cols, rows) in dict
                    self.min_values[min] = [cols, rows]

        # Return dict with minimal values
        return self.min_values


    # Function for run algorithm
    def start_algorithm(self, depth = 0):

        # Exit from function if dict with minimal values is empty
        if self.min_values == None:

            return

        # Assign minimal key from dict
        min_key = min(self.min_values.keys())

        key, value = self.min_values[min_key]

        # Delete element from dict
        del self.min_values[min_key]

        summ = sum( self.matrix[ depth ] ) - self.matrix[ value[0], value[1] ]



    # This function show matrix on display
    def show_matrix(self):

        print ( self.matrix )


if __name__ == "__main__":

    matrix = GreedyAlgorith(3)

    matrix.set_matrix()

    matrix.show_matrix()

    min_values = matrix.get_min()

    print("Min values: ", min_values )
