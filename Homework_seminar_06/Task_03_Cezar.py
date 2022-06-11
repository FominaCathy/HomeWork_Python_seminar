#3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. 
# ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . 
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.




def rot13(in_txt, code):

    alfa_list = [chr(i) for i in range(65, 91)] # 26 символов
    
    output_text =""
    for ch in in_txt:
        if ch.isalpha() == True:
            txt = (ord(ch.upper())-65 + 13*code)%25
            if ch.isupper() == True:
                output_text =  output_text + str(alfa_list[txt])
            else:
                output_text =  output_text + str(alfa_list[txt].lower())
        else:
            output_text =  output_text + ch
    return output_text


input_text = "Mom - was washing the frame"
print(input_text)
out_text = rot13(input_text, 1)
print(out_text)

print(rot13(out_text, -1))
