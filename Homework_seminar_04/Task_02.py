# Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя


input_list = [1, 2, 5, 3, 4, 6, 1, 7]
len_list = len(input_list)
index_list = [1]*len_list
i = 0
len_list = len(input_list)
for i  in range(0, len_list):
    j = 0
    for j in  range(0, i+1):
	    if (input_list[j] < input_list[i]):
		    index_list[i] = max (index_list[i], index_list[j] + 1)

count_elements = max(index_list) # кол-во элементов в подпоследовательностиы
i = index_list.index(count_elements) # индех последнего элемента в последовательности
max_sublist = []

temp = input_list[i] # мах элемент в нашей последовательности
max_sublist.append(temp)

count_elements -= 1
while count_elements > 0:
    
    while index_list[i] != count_elements:
        i -= 1
    if temp > input_list[i]:
        max_sublist.insert(0, input_list[i])
        temp = input_list[i]
        count_elements -= 1

print(f"мах. подпоследовательность: {max_sublist}") 

