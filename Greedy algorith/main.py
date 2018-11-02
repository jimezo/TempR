import math # math.inf
import copy # copy.deepcopy()

class GreedyAlgorith:

    # Function contractor
    def __init__(self, matrix):

        self.size = 0 # Variable there save matrix size

        self.matrix = matrix # List there save matrix

        self.min_values = []

        self.result = 0


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


    def reduction_rows(self, matrix, min_in_rows):

        for rows in range( self.size ):

            for cols in range( self.size ):

                matrix[rows][cols] -= min_in_rows[rows]

        return matrix


    def reduction_cols(self, matrix, min_in_cols):

        for rows in range( self.size ):

            for cols in range( self.size ):

                matrix[cols][rows] -= min_in_cols[rows]

        return matrix


    def find_null_values( self, matrix ):

        null_values = {}

        count = 0

        for rows in range( self.size ):

            for cols in range( self.size ):

                if matrix[rows][cols] == 0:

                    val = matrix[rows][cols]

                    null_values[ 'val_' + str(count) ] = [ rows, cols ]

                    count += 1

        return null_values


    # Function for calculate evaluation from rows and column where matrix element == 0
    def find_evaluation(self, matrix, null_values):

        min_in_rows = []

        min_in_cols = []

        evaluations = {}

        count = 0

        for val in null_values.values():

            min_in_rows.clear()

            min_in_cols.clear()

            for elem in range( self.size ):

                if elem != val[1]:

                    min_in_rows.append( matrix[ val[0] ][elem] )

                if elem != val[0]:

                    min_in_cols.append( matrix[ elem ][ val[1] ] )

            min_val_col = min( min_in_cols )

            min_val_row = min( min_in_rows )

            eval = min_val_col + min_val_row

            evaluations[ count ] = {'eval': eval, 'pos': [val]}

            count += 1

        return evaluations


    # This function find minimal value from matrix and return dict with minimal value
    def get_min(self):

        min_in_rows = []

        min_in_cols = []

        matrix = copy.deepcopy( self.matrix )

        # Find minimal values from rows
        for rows in range( self.size ):

            min_in_rows.append( min( matrix[rows] ) )

        matrix = self.reduction_rows( matrix, min_in_rows)

        for rows in range( self.size ):

            col = []

            for cols in range( self.size ):

                col.append( matrix[cols][rows] )

            min_in_cols.append( min(col) )

        matrix = self.reduction_cols( matrix, min_in_cols)

        self.min_values.append( min_in_rows )
        self.min_values.append( min_in_cols )

        return matrix


    def max_evaluation(self, evaluation):

        evals = []

        for eval in evaluation.values():

            evals.append( [eval['eval'], eval['pos'][0] ] )

        try:

            return max( evals )

        except:

            return


    def check_inf(self, elem, matrix):

        count_inf_on_cols = 0

        count_inf_on_rows = 0

        for index in range( self.size ):

            if matrix[ elem[0] ][ index ] == math.inf:

                count_inf_on_cols += 1

            if matrix[ index ][ elem[1] ] == math.inf:

                count_inf_on_rows += 1

        if count_inf_on_cols >= 2 or count_inf_on_rows >= 2:

            return True

        return False


    # Strike out rows and cols on position elem, where have two 'inf'
    def strike_out(self, elem, matrix):

        for index in range( self.size ):

            matrix[ elem[0] ][ index ] = math.inf

            matrix[ index ][ elem[1] ] = math.inf

        return matrix


    def is_null(self, matrix):

        for rows in range( self.size ):

            for cols in range( self.size ):

                if matrix[rows][cols] != math.inf:

                    return False

        return True


    def calculate_result(self, evaluation, matrix):

        while True:

            max_eval = self.max_evaluation( evaluation )

            if max_eval == None:

                break

            if matrix[ max_eval[1][0] ][ max_eval[1][1] ] != math.inf:

                print(str(self.result) + ' + ' + str( matrix[ max_eval[1][0] ][ max_eval[1][1] ] ))

                self.result += matrix[ max_eval[1][0] ][ max_eval[1][1] ]

            matrix[ max_eval[1][0] ][ max_eval[1][1] ] = math.inf

            if self.check_inf(max_eval[1], matrix):

                matrix = self.strike_out( max_eval[1], matrix )

                # Delete item from evaluation
                for key in evaluation.keys():

                    elem = evaluation[key]['pos']

                    if matrix[ elem[0][0] ][ elem[0][1] ] == math.inf:

                        evaluation.pop(key)

                        break

            if evaluation == None:

                return None

        return matrix


    # Function for run algorithm
    def start_algorithm(self):

        self.size = len( self.matrix )

        self.show_matrix()

        while True:

            matrix = self.get_min()

            null_values = self.find_null_values( matrix )

            evaluation = self.find_evaluation(matrix, null_values)

            M = self.calculate_result(evaluation, self.matrix)

            if self.is_null(M):

                break

        print("Changed matrix: ", matrix)
        print ("Min in rows: ", self.min_values[0])
        print ("Min in cols: ", self.min_values[1])
        print("Null values: ", null_values )
        print("Result: ", self.result)
        print('M: ', M)

    # This function show matrix on display
    def show_matrix(self):

        print ('Original matrix: ', self.matrix )


if __name__ == "__main__":

    M = [

        [ math.inf, 5, 11, 9 ],
        [ 10, math.inf, 8, 7 ],
        [ 7, 14, math.inf, 8 ],
        [ 12, 6, 15, math.inf ],

    ]

    matrix = GreedyAlgorith(M)

    matrix.start_algorithm()
