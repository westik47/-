# расчет размера пенсии

from colorama import init, Fore, Back, Style
import time
init()

def console_picture():
    print(Style.BRIGHT + Fore.BLUE)
    print("                ,__,       ")
    print("   Пенсия 1.4   (oo)____   ")
    print("                (__)    )\  ")
    print("                   ||--|| *")
 

console_picture()

print(Style.BRIGHT + Fore.YELLOW)
a = int(input("Оклад по должности: ")) + int(input("Оклад по званию: ")) # оклад плюс звание
b = a * int(input("Процентная надбавка за выслугу лет: ")) / 100 # умножаю полученный резульат на процентную надбавку за выслугу лет 
x = a + b 
c = x * 0.7368
d = c * float(input("Размер пенсии в процентах: ")) / 100
print(Style.DIM + Fore.RED)
print ("Размер выплаты: ", (d), ("₽"))
time.sleep(5)


