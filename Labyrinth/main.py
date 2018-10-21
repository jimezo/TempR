# http://acmp.ru/index.asp?main=task&id_task=99

from random import randint

from numpy import array


class Labyringth:

    def __init__(self):

        self.Levels = []

        self.count_columns_on_level = 3

        self.prince_location = { 'level': 0, 'location': [] }

        self.count_rows = 0

        self.count_columns = 0


    def add_columns(self, level):

        columns_locations = []

        while True:

            column = [ randint(self.count_rows, self.count_columns), randint(self.count_rows, self.count_columns) ]

            if column not in columns_locations:

                columns_locations.append(column)

            else:

                continue

            if len(columns_locations) == self.count_columns_on_level:

                break

        for column in columns_locations:

            self.Levels[level][column[0]][column[1]] = 'o'


    def set_labyrinth(self, count_level, labyrinth_height, labyrinth_width):

        if ( int(count_level) < 2 and int(labyrinth_height), int(labyrinth_width) > 50 ):

            return False

        self.count_levels = int(count_level)

        for level in range(int(count_level)):

            self.Levels.append( array(labyrinth_height, labyrinth_width) )

            if ( level + 1 == 1 ):

                self.Levels[level][0][0] = '1'

                self.prince_location['location'] = [0, 0]

            if ( level + 1 == int(count_level) ):

                princess_location = [ randint(self.count_rows, self.count_columns), randint(self.count_rows, self.count_columns) ]

                self.Levels[ level ][ princess_location[0] ][ princess_location[1] ] = '2'

            self.add_columns( level )


    def break_the_floor(self):

        self.prince_location['location'] = 
