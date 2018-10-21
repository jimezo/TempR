# http://acmp.ru/index.asp?main=task&id_task=29

from math import fabs
from random import randint

class Heroes:

    def __init__(self):

        self.current_platform = 0
        self.energy = 0
        self.heroes_coordinate = 0
        self.platforms = []


    def generate_platforms(self, count_platform, min_height, max_height):

        if ( count_platform < 1 and count_platform > 30000 ):
            return False

        for platform in range(count_platform):

            self.platforms.append( randint( int(min_height), int(max_height) ) )

        self.heroes_coordinate = self.platforms[ self.current_platform ]


    def set_platforms(self, count_platform, platform_list):

        for platform_index in range(int( count_platform )):
            self.platforms.append( platform_list[ platform_index ] )

        self.heroes_coordinate = self.platforms[ self.current_platform ]

    def jump(self):

        try:
            self.energy += self.platforms[ self.current_platform + 1 ] - self.heroes_coordinate
        except:
            return True
        else:
            self.heroes_coordinate = self.platforms[ self.current_platform + 1]
            self.current_platform += 1


    def super_jump(self):

        try:
            self.energy += ( self.platforms[ self.current_platform + 2 ] - self.heroes_coordinate ) * 3
        except:
            return True
        else:
            self.heroes_coordinate = self.platforms[ self.current_platform + 2 ]
            self.current_platform += 2


    def calculate_energy(self):

        current_platform = 0
        next_platform = 1
        next_next_platform = 2

        for platform in range(len(self.platforms)):

            n_energy = 0
            nn_energy = 0

            try:
                n_energy = self.platforms[next_platform] - self.platforms[current_platform]
            except: n_energy = 30001

            try:
                nn_energy = self.platforms[next_next_platform] - self.platforms[current_platform]
                between_n_nn = n_energy + ( self.platforms[next_next_platform] - self.platforms[current_platform] )
            except: nn_energy = 30001

            if (n_energy < nn_energy):
                self.jump()
                current_platform += 1
                next_platform += 1
                next_next_platform += 1
            elif (between_n_nn > nn_energy):
                self.super_jump()
                current_platform += 2
                next_platform += 2
                next_next_platform += 2

            if (current_platform + 1 == len(self.platforms)):
                break

        return fabs(self.energy)



if __name__ == '__main__':

    platforms = [1,5,2]

    heroes = Heroes()
    heroes.set_platforms(3, platforms)
    energy = heroes.calculate_energy()
    print(energy)
