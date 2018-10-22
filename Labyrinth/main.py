# http://acmp.ru/index.asp?main=task&id_task=99

from random import randint

from numpy import array

from time import sleep


class Labyringth:

    def __init__(self):

        self.Levels =  []

        self.count_columns_on_level = 3

        self.prince_location = { 'level': 0, 'location': [] }

        self.count_rows = 0

        self.count_columns = 0

        self.count_levels = 0


    def add_columns(self, level):

        columns_locations = []

        while True:

            column = [ randint(0, self.count_columns - 1),
                    randint(0, self.count_columns - 1)
                    ]

            if column not in columns_locations:

                columns_locations.append(column)

            else:

                continue

            if len(columns_locations) == self.count_columns_on_level:

                break

        for column in columns_locations:

            self.Levels[level][column[0]][column[1]] = 'o'


    def fill_matrix(self, count_level, height, width):

        new_level = []

        for rows in range(height):

            new_level.append( list('.') * width )

        return new_level


    def print_labyrinth(self):

        line = str()

        for level in range( self.count_levels ):

            for rows in range( self.count_rows ):

                if rows == 0:

                    print('\n')

                for cols in range( self.count_columns ):

                    line += self.Levels[level][rows][cols] + ' '

                    if cols == self.count_columns - 1:

                        print ( line )

                        line = ''



    def set_labyrinth(self, count_level, labyrinth_height, labyrinth_width):

        if ( int(count_level) < 2 and int(labyrinth_height) > 50 and int(labyrinth_width) > 50):

            return False

        self.count_rows, self.count_columns = labyrinth_height, labyrinth_width

        self.count_levels = int(count_level)

        for level in range(int(count_level)):

            new_level = self.fill_matrix(count_level, labyrinth_height, labyrinth_width)

            self.Levels.append( new_level )

            if ( level + 1 == 1 ):

                self.Levels[level][0][0] = '1'

                self.prince_location['location'] = [0, 0]

            if ( level + 1 == int(count_level) ):

                princess_location = [ randint(0, self.count_columns - 1), randint(0, self.count_columns - 1) ]

                self.Levels[ level ][ princess_location[0] ][ princess_location[1] ] = '2'

            self.add_columns( level )

        self.print_labyrinth()


    def find_free_location( level ):

        for rows in range(self.count_rows):

            for cols in range(self.count_columns):

                if ( level[rows][cols] == '.' ):

                    return list(rows, cols)


    def break_the_floor(self):

        try:

            self.prince_location['location'] = find_free_location( self.Level[self.prince_location['level'] + 1] )

            delay = ( (self.count_rows * self.count_columns) - (self.prince_location['location'][1] * self.prince_location['location'][0] ) ) / 60

            sleep(delay)

            return True

        except:

            return False


    def analysis_level(self):

        best_way = []

        all_ways = []

        way = []

        for rows in range( self.count_rows ):

            for cols in range( self.count_columns ):

                if ( self.Levels[rows][cols] == '.' ):

                    way.append( list(rows, cols) )

                if self.Levels[rows][cols] == '2':

                    best_way.append( list(rows, cols) )

                    return best_way

                else:

                    if way:

                        all_ways.append( list(cols, rows) )

                    way.clear()

        if best_way:

            return best_way

        for way_num in range(len(all_ways)):

            try:

                if all_ways[way_num][1] > all_ways[way_num + 1 ][1]:

                    best_way.clear()

                    best_way.append( all_ways[way_num] )

            except:

                break

        return best_way


    def prince_move(self):

        best_way = analysis_level()

        delay = 1

        for way in best_way:

            old_location = self.prince_location['location']

            self.prince_location['location'] = lisT( way[0], way[1] )

            self.Levels[ way[0], way[1] ] = self.prince_location['location']

            self.Levels[ old_location ] = '.'

            sleep( delay )

        if self.prince_location['location'][1] < self.count_rows:

            self.break_the_floor()


if __name__ == '__main__':

    labyrinth = Labyringth()
    labyrinth.set_labyrinth(3, 3, 3)
