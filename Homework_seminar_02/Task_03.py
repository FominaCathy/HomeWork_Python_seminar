# В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def difference(array):
    import math
    min_number = 0
    max_number = 0

    for i in array:
        if str(i).find(".") != -1: # проверяем есть ли вещ.часть и выделяем ее
            temp = str(i)[str(i).find(".")+1: len(str(i))]
            float_part = int(temp)/(10**(len(str(i))- str(i).find(".")-1))
            print(float_part)        
            if  min_number == 0:
                    min_number = float_part
            else:
                min_number = min(min_number,float_part)
            max_number = max(max_number,float_part)
    if (min_number == 0) and (max_number == 0) :
        print("дробных частей нет")
    else:
        print(f"разница между мин. ({min_number}) и макс. ({max_number}) значением дробной части = {max_number - min_number}")

arr = [1.1, 1.2, 3.1, 5, 10.01]
print(arr)
difference(arr)

arr = [1, 1, 3, 5, 10]
print(arr)
difference(arr)


