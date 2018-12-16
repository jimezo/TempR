import math

class GreedyAlgorithm():

    def __init__(self):

        self.matrix = []
        self.matrix_size = 0
        self.debug = False
        self.ways = dict()
        self.result = list()
        self.letters = list()
        self.values = list()

    def initMatrix(self):

        self.matrix_size = int(input('Count city: '))
        for char in range(self.matrix_size):
            self.letters.append( chr(65 + char) )

        # Debug
        if self.debug:
            print('LETTERS = ', self.letters)

        for from_city in range(self.matrix_size):
            way = dict()
            for to_city in range(self.matrix_size):

                if from_city == to_city or to_city < from_city:
                    continue

                distance = int(input('{} -> {} = '.format(self.letters[from_city], self.letters[to_city])))
                way[self.letters[to_city]] = distance

            if self.debug:
                print('WAY = ', way)

            self.ways[self.letters[from_city]] = way

        if self.debug:
            print('WAYS = ', self.ways)


    def set_sity(self):
        from_to = input('Set from-to sity: ')
        split_letter = from_to.split('-')
        if self.debug:
            print('SPLIT LETTER = ', split_letter)
        return split_letter


    def analysis(self, from_to):
        peaks = list()
        prev_letters = ''
        for from_city in self.ways.keys():

            if ord(from_to[0]) > ord(from_city):
                continue

            prev_letters += from_city + ';'
            for to_city in self.ways[from_city].keys():
                if from_to[1] == to_city:
                    peaks.append([prev_letters+to_city])

        if self.debug:
            print('PEAKS = ', peaks)

        return peaks


    def findMin(self, ways):
        values = dict()
        for way in range(len(ways)):
            letters = ways[way][0].split(';')
            value = 0
            for letter in range(len(letters)):
                try:
                    value += self.ways[ letters[letter] ][ letters[letter + 1] ]
                except IndexError:
                    pass

                if letter+1 == len(letters):
                    values[ ways[way][0] ] = value

        if self.debug:
            print('KEYS = ', values.keys())
            print('VALUES = ', values.values())

        min_val = math.inf
        for lett in values.keys():
            if values[lett] < min_val:
                min_val = values[lett]
                self.result = [lett, min_val]

        if self.debug:
            print('RESULT = ', self.result)

        return self.result


    def Calculate(self, from_to):

        ways = self.analysis(from_to)
        way = self.findMin(ways)
        letters = ''
        short_way_lett = way[0].split(';')
        for swl in range(len(short_way_lett)):
            if swl+1 != len(short_way_lett):
                letters += short_way_lett[swl] + ' -> '
            else:
                letters += short_way_lett[swl]

        self.result = [letters, way[1]]

        return self.result


    def run(self):
        self.initMatrix()
        self.Calculate( self.set_sity() )
        print(self.result)

if __name__ == '__main__':
    GreedyAlgorithm().run()