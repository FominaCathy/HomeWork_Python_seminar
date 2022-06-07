# Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. 
# Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»
# результат: "гдеж рабав копыто ф Абкн абрыволк олк"

exe_text = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
sub_text = "абв" # удаляемая строка
len_remove = len(sub_text) # длина удаляемой строки

in_point = lambda: exe_text.lower().find(sub_text.lower())
remove_text = lambda in_txt, a, b : in_txt[:a] + (in_txt[(a + b):])

while in_point() != -1:
    #exe_text = exe_text[:in_point()] + exe_text[(in_point()+len_remove):]
    exe_text = remove_text (exe_text, in_point(), len_remove )
print(exe_text)
