import math # math.inf

class GreedyAlgorith:

    # Function contractor
    def __init__(self, size = 0):

        self.size = size # Variable there save matrix size

        self.matrix = [        # List there save matrix

                    [ math.inf, 5, 11, 9 ],
                    [ 10, math.inf, 8, 7 ],
                    [ 7, 14, math.inf, 8 ],
                    [ 12, 6, 15, math.inf ],

                ]

        self.min_in_rows = []

        self.min_in_cols = []

        self.optimal_way = {}


    def set_matrix(self):

        for cols in range( self.size ):

            row = []

            for rows in range( self.size ):

                # Cols and rows not can cross yorself, so, add 0 to matrix and pass next value
                if cols == rows:

                    row.append( math.inf )

                    continue

                value = int( input("Enter value for ["+ str(cols) +"][" + str(rows) +"]: \t\n > ") )

                row.append( value )

            self.matrix.append( row )


    def reduction_rows(self, matrix):

        for rows in range( self.size ):

            for cols in range( self.size ):

                matrix[rows][cols] -= self.min_in_rows[rows]

        return matrix


    def reduction_cols(self, matrix):

        for rows in range( self.size ):

            for cols in range( self.size ):

                matrix[cols][rows] -= self.min_in_cols[rows]

        return matrix
        

    def find_null_values( self, matrix ):

        null_values = {}

        for rows in range( self.size ):

            for cols in range( self.size ):

                if matrix[rows][cols] == 0:

                    val = matrix[rows][cols]

                    null_values[ 'val_' + str(rows) ] = [ rows, cols ]

        return null_values


    # This function find minimal value from matrix and return dict with minimal value
    def get_min(self):

        if self.size == 0:

            self.size = len(self.matrix)

        matrix = self.matrix.copy()

        # Find minimal values from rows
        for rows in range( self.size ):

            self.min_in_rows.append( min( matrix[rows] ) )

        matrix = self.reduction_rows( matrix )

        for rows in range( self.size ):

            col = []

            for cols in range( self.size ):

                col.append( matrix[cols][rows] )

            self.min_in_cols.append( min(col) )

        matrix = self.reduction_cols( matrix )

        null_values = self.find_null_values( matrix )

        print("Changed matrix: ", matrix)
        print ("Min in rows: ", self.min_in_rows)
        print ("Min in cols: ", self.min_in_cols)
        print("Null values: ", null_values )


    # Function for run algorithm
    def start_algorithm(self):

        matrix.show_matrix()

        matrix.get_min()


    # This function show matrix on display
    def show_matrix(self):

        print ('Original matrix: ', self.matrix )


if __name__ == "__main__":

    matrix = GreedyAlgorith()

    matrix.start_algorithm()
