import math


def matrix_to_graph(matrix):
    graph = dict()
    for cols in range(size):
        for rows in range(size):
            print(matrix[cols][rows])


def set_matrix_size():
    while True:
        size = int(input('Размер матрицы: '))
        if size > 0:
            return size


def init_matrix(size):
    matrix = list()
    for cols in range(size):
        row = list()
        for rows in range(size):

            if rows == cols:
                row.append(math.inf)
                continue

            while True:
                value = int(input('Enter matrix [{}][{}]: '.format(cols+1, rows+1)))
                if value > 0:
                    row.append(value)
                    break

        matrix.append(row)

    return matrix


def run():
    matrix_size = set_matrix_size()
    matrix = init_matrix(matrix_size)
    graph = matrix_to_graph(matrix)


if __name__ == '__main__':
    run()