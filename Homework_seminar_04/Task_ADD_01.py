# Пирамида пивных банок будет квадратировать количество банок на каждом уровне
#  - 1 банка на верхнем уровне, 4 на втором, 9 на следующем, 16, 25...
#Определите функцию beeramid, чтобы вернуть количество полных уровней пирамиды пивных банок, 
# которую вы можете сделать, учитывая параметры: реферальный бонус и цена пивной банки.
# Например:
# beeramid(1500, 2)# 12
# beeramid(5000, 3)# 16

def beeramid(bonus, price):
    count = bonus//price # кол-банок, которое можем купить
    