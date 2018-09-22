import random, time

# Кол-во элементов
COUNT = 40000

# Пустой список
array = []

# Заполнение списка
print('start append list')
for element in range(COUNT):
    array.append(random.randint(0, 1000))
print('end append list')

start_time = time.time()

# Сортировка списка
print('start sort list')
k = 1
while k < len(array):
     for i in range(len(array)-k):
          if array[i] > array[i+1]:
               array[i],array[i+1] = array[i+1],array[i]
     k += 1
print('end sort list')
print("--- %s seconds ---" % (time.time() - start_time))

print(array)
