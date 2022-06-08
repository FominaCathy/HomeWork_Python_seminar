#4. Создайте два списка — один с названиями языков программирования, 
# другой — с числами от 1 до длины первого плюс 1. 
# Вам нужно сделать две функции: 
# первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами. 
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков. 
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. 
# С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.

from turtle import ycor
from functools import reduce

language_pro = ["Basic", "Pascal", "HPL", "Java", "Python", "Assembly", "C++", "C#", "PHP"] # список языков исходный

numbers_list = [i for i in range(1, len(language_pro)+1)]

# переведем список языков в верхний регистр для дальнейшей с ним работы
language_pro = [language_pro[i].upper() for i in range(0, len(language_pro)) ] 

list_cortege = list(zip(numbers_list, language_pro)) # объеденение с помощью zip
print (list_cortege)

def summ_number (element):
    item = [ord(ch) for ch in element]
    summ_ch = reduce(lambda x, y : x + y, item)
    return summ_ch

list_bonus = [(summ_number(language_pro[i]),language_pro[i])  for i in range(0, len(language_pro))] 
print(list_bonus)
#отфильтруем
            
res_list = list(filter(lambda x: x[0]%(list_bonus.index(x)+1) == 0, list_bonus))
print("отфильтрованный список")
print(res_list)

