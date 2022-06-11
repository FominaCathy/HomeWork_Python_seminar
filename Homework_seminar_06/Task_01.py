#1 -  Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;



def select_operation(choice):
    if choice == 0:
        return lambda a, b: a + b
    elif choice == 1:
        return lambda a, b: a - b
    elif choice == 2:
        return lambda a, b: a * b
    elif choice == 3:
        return lambda a, b: a / b  
    elif choice == 4:
        return lambda a, b: a ** b      

def marsh_yard (exe_str):
    RPN_lst = []
    stek = ""
    temp = ""
    prior = lambda op : list_prioritet[list_operation.index(op)]
    for ch in exe_str:
        if ch.isdigit() == True:
            temp = temp + ch
        elif ch == "(":
            stek = stek + ch
        elif ch == ")":
            RPN_lst.append(temp)
            temp =""
            while stek[-1] != "(":
                RPN_lst.append(stek[-1])
                stek = stek[0:len(stek)-1]
            stek = stek[0:len(stek)-1]
        else:
            if temp != "" :
                RPN_lst.append(temp)
                temp =""
            if (stek == "")or(stek[-1] == "("): stek = stek + ch
            else: 
                if prior(ch) >= prior(stek[-1]):
                    RPN_lst.append(stek[-1])
                    stek = stek[0:len(stek)-1] + ch
                else:
                    stek = stek + ch

    if temp != "": RPN_lst.append(temp)
    if stek !="": RPN_lst.append(stek)
    

    return RPN_lst 

def calc_RPN(RPN_lst):

    stek = []
    step = 0
    temp = 0
    for i in RPN_lst:
        if i.isdigit() == True:
            stek.append(i)
            
        else: 
            operation = select_operation(list_operation.index(i)) 
            step = len(stek)-1
            temp = operation(int(stek[step-1]),int(stek[step]))
            stek.pop()
            stek[-1] = temp
        
    return stek[len(stek)-1]


list_operation = ['+', '-', '*', '/', '^']
list_prioritet = [3, 3, 2, 2, 1]

exe_string = "(6+10-4)^2/(1+1*2)+1"
temp = exe_string.replace(" ", "")

RPN_list = marsh_yard (exe_string)
print(marsh_yard (exe_string))


print(calc_RPN(RPN_list))

 

