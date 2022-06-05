# Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию. 
# сортировку написать самостоятельно

import random

def quick_sort(list_d, start, end): # быстрая сортировка 

    if start < end:

        left = start
        right = end
        pivot = list_d[random.randint(start,end)] 

        while (left <= right):
            while (list_d[left] < pivot):
                left += 1
            while list_d[right] > pivot:
                right -= 1 
            
            if left <= right:
                list_d[left], list_d[right] = list_d[right], list_d[left]
                left += 1
                right -= 1 

        quick_sort(list_d, start, right) # сортируем левую часть
        quick_sort(list_d, left, end) # сортируем правую часть

    else:
        return 


with open("file.txt", "w") as data_file: # заполняем файл случайными числами
    for i in range(0,10):
        data_file.write(str(random.randint(1, 101)) + '\n')

list_data = []

with open("file.txt", "r") as data_file: # записываем данные из файла в список
    for line in data_file:
        list_data.append(int(line))
    
quick_sort(list_data, 0, len(list_data)-1) # сортируем список

with open("file.txt", "w") as data_file: # перезаисываем файл отсротированными числами
    for i in list_data:
        data_file.write(str(i) + '\n')

