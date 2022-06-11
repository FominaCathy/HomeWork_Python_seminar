# 2 - Реализовать RLE алгоритм. 
# реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах 


exe_text = "AAAAAAAAAAAABCDEBBBBBBBBBBBBBBBBBBBBBBDDELSR"

def rle_code(input_text):

    arh_text_list = [] # символ или цепочка которые идут в архив
    output_text = ""
    temp_txt = "" 
    temp_len_txt = 0
    for ch in input_text:
        if temp_txt == "":  
            temp_txt = ch
        elif temp_txt == ch: 
            temp_len_txt += 1
        else:
            arh_text_list.append((temp_len_txt,temp_txt))
            temp_txt = ch 
            temp_len_txt = 0    
    
    arh_text_list.append((temp_len_txt,temp_txt))

    temp_txt = ""
    for pair in arh_text_list:
        if pair[0] != 0: 
            if temp_txt != "":
                output_text = output_text + "0" + str(len(temp_txt)-1) + temp_txt
                temp_txt = ""
            output_text = output_text + "1" + str(pair[0]) + str(pair[1])
        elif pair[0] == 0: 
            temp_txt = temp_txt + str(pair[1])

    if temp_txt != "":
        output_text = output_text + "0" + str(len(temp_txt)-1) + temp_txt
        temp_txt = ""


    return output_text

def rle_decode (input_text):
    i = 0
    
    output_text = ""
    while i < len(input_text):
        k = 1 
        if int(input_text[i]) == 0: 
            
            while input_text[i+1:i+k+1].isnumeric() == True: k += 1
            temp = int(input_text[i+1:i+k])+1

            output_text = output_text + input_text[i+k:i+k+temp]
            i += k + temp
        elif int(input_text[i]) == 1: #повторяющаяся последовательность
            while input_text[i+1:i+k+1].isnumeric() == True: k += 1
            temp = int(input_text[i+1:i+k])+1 

            output_text = output_text + str(input_text[i+k:i+k+1]*(temp))
            i += k + 1
    return output_text


with open("primary.txt", "w") as base_txt: #записали в файл
    base_txt.write("AAAAAAAAAAAABCDEBBBBBBBBBBBBBBBBBBBBBBDDELSR")

with open("primary.txt", "r") as base_txt: #считали из файла
    exe_text = base_txt.read()

print(exe_text) #печать исходного текста

out_txt = rle_code(exe_text) # сжатие текста

print(out_txt ) # печать сжатого текста

#запишем сжатый текст в новый  файл
with open("rle.txt", "w") as base_txt: #записали в файл
    base_txt.write(out_txt)

with open("rle.txt", "r") as base_txt: #считали из файла
    out_text = base_txt.read()

print(rle_decode(out_txt))
    

