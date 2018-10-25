# http://acmp.ru/index.asp?main=task&id_task=99

from random import randint

from numpy import array

from time import sleep


class Labyringth:

    def __init__(self):

        self.Levels =  []

        self.count_columns_on_level = 6

        self.prince_location = { 'level': 0, 'location': [] }

        self.princess_location = 0

        self.count_rows = 0

        self.count_columns = 0

        self.count_levels = 0

        self.ways = []


    def add_columns(self, level):

        columns_locations = []

        while True:

            column = [ randint(0, self.count_columns - 1),
                    randint(0, self.count_columns - 1)
                    ]

            if column not in columns_locations:

                if level + 1 == 1:

                    if column != self.prince_location['location']:

                        columns_locations.append(column)

                elif level + 1 == self.count_levels:

                    if column != self.princess_location:

                        columns_locations.append(column)

                else:

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

                self.princess_location = [ randint(0, self.count_columns - 1), randint(0, self.count_columns - 1) ]

                self.Levels[ level ][ self.princess_location[0] ][ self.princess_location[1] ] = '2'

            self.add_columns( level )

        self.print_labyrinth()


    def find_free_location(self, level ):

        for rows in range(self.count_rows):

            for cols in range(self.count_columns):

                if ( self.Levels[ level ][ rows ][ cols ] == '.' ):

                    return [rows, cols]


    def break_the_floor(self):

        try:

            self.prince_location['level'] += 1

            self.prince_location['location'] = self.find_free_location( self.Level[self.prince_location['level']] )

            return True

        except:

            return False


    def check_princess(self, level, prince_location ):

        try:

            if (self.Levels[ level ][ prince_location[0] ][ prince_location[1] ] == '2' ):

                return True

            if (self.Levels[ level ][ prince_location[0] + 1 ][ prince_location[1] ] == '2' ):

                return True

            if (self.Levels[ level ][ prince_location[0] ][ prince_location[1] + 1 ] == '2' ):

                return True

            if (self.Levels[ level ][ prince_location[0] - 1 ][ prince_location[1] ] == '2' ):

                return True

            if (self.Levels[ level ][ prince_location[0] ][ prince_location[1] - 1] == '2' ):

                return True

        except:

            return False


    def move(self, ways, prince, depth = 0):

        self.prince_location['location'] = prince

        print('Location: ' , self.prince_location['location'])

        if (prince[0] + 1 == self.count_rows and self.prince_location['level'] < self.count_levels):

            return True

        level = self.prince_location['level']

        if ( level + 1 == self.count_levels ):

            if self.check_princess( level, prince ):

                return True

        if ( depth == len(ways) ):

            return False

        if ( [ prince[0] + 1, prince[1] ] in ways ):

            self.ways.append( [ prince[0] + 1, prince[1] ] )

            self.move(ways, [ prince[0] + 1, prince[1] ], depth + 1 )

            return True

        if ( [ prince[0], prince[1] + 1 ] in ways ):

            self.ways.append( [ prince[0], prince[1] + 1 ] )

            self.move(ways, [ prince[0], prince[1] + 1 ], depth + 1 )

            return True

        if ( [ prince[0] - 1, prince[1] ] in ways ):

            self.ways.append( [ prince[0] - 1, prince[1] ] )

            self.move(ways, [ prince[0] - 1, prince[1] ], depth + 1 )

            return True

        if ( [ prince[0], prince[1] - 1 ] in ways ):

            self.ways.append( [ prince[0], prince[1] - 1 ] )

            self.move(ways, [ prince[0], prince[1] - 1 ], depth + 1 )

            return True


    def analysis_level(self, level):

        best_way = []

        all_ways = []

        way = []

        for rows in range( self.count_rows ):

            for cols in range( self.count_columns ):

                if self.Levels[level][rows][cols] == '.' or self.Levels[level][rows][cols] == '2':

                    way.append( [rows, cols] )

        for way_num in range(len(way)):

            try:

                if way[way_num][0] > way[way_num + 1 ][0]:

                    best_way.clear()

                    best_way.append( way[way_num] )

                elif way[way_num][0] < way[way_num + 1 ][0]:

                    best_way.clear()

                    best_way.append( way[way_num + 1] )

            except:

                pass

        if not self.move(way, self.prince_location['location']):

            self.break_the_floor()

        else:

            if level + 1 < self.count_levels:

                x,y = self.find_free_location( level + 1 )

                self.prince_location['level'] += 1

                self.prince_location['location'] = [x,y]

            elif ( level + 1 == self.count_levels ):

                if self.check_princess( level, self.prince_location['location'] ):

                    print('\n\n')

                    return True

        print('\n\n')

        return False


    def prince_move(self):

        for level in range( self.count_levels ):

            if self.analysis_level( level ):

                print('Prince find princess')

                break

            self.ways.clear()



if __name__ == '__main__':

    labyrinth = Labyringth()
    labyrinth.set_labyrinth(3, 4, 4)
    labyrinth.prince_move()
