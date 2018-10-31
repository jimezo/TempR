from pprint import pprint # модуль pprint используется для удобного вывода на экран
strings=3
matrix=[[0,5,11,9,],
        [10,0,8,7],
        [7,14,0,8],
        [12,6,15,0]]
matrix_t=[]
i=0
print(matrix)
#MATRIX FILL (using only if algorithm recorded)
# ------------------------------------------------------------------------------
# for number in range(strings):
#     matrix.append(input())
# while i<strings:
#     matrix_t.append(matrix[i].split(","))
#     i=i+1
# i=0
# l=0
# matrix.clear()
#
# First itteration
# ------------------------------------------------------------------------------
matrix_copy=matrix.copy()
di=[]
buff=[]

while i<len(matrix):
    buff.append(sorted(matrix[i]))
    di.append(buff[i][1])
    i=i+1

i=0
buff.clear()
print(di)
# Second itteration
#-------------------------------------------------------------------------------
n=0
buff1=[]
matrix_red=[]
while n<len(matrix):
    while i<len(matrix):
        if matrix[n][i]>di[n]:
            matrix_red.append(matrix[n][i]-di[n])
        else:
            matrix_red.append(0)
        i=i+1
    n=n+1
    i=0
n=0
i=0
g=0
len_matrix=len(matrix_red)**2#Количество элементов

for number in range (len(matrix)):
    buff1.append([matrix_red[g],matrix_red[g+1],matrix_red[g+2],matrix_red[g+3]])
    i=i+1
    g=g+4
matrix_red=buff1.copy()
# third itteration
# ------------------------------------------------------------------------------
n=0
i=0
dj=[]
buff.clear()
