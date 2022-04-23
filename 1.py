# расчет размера пенсии

from colorama import init, Fore, Back, Style
import time
import sys
import itertools
import threading

init()
print(Style.DIM + Fore.RED)
print("Загрузка:")
animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
#animation = ["[т]","[те]", "[тек]", "[текс]", "[текст]", "[тексто]", "[текстов]", "[текстовы]", "[текстовый]", "текстовый1"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")

def console_picture():
    print(Style.BRIGHT + Fore.BLUE)
    print("                ,__,       ")
    print("   Пенсия 1.4   (oo)____   ")
    print("                (__)  ₽ )\  ")
    print("                   ||--|| *")

console_picture()

print(Style.BRIGHT + Fore.YELLOW)
a = int(input("Оклад по должности: ")) + int(input("Оклад по званию: ")) # оклад плюс звание

def console_picture():
	print(Style.DIM + Fore.RED)
	print("Процентная надбавка за выслугу лет к окладам денежного содержания:")
	print(Style.BRIGHT + Fore.YELLOW)
	print("От 2 до 5 лет   – 10%       От 15 до 20 лет   – 25%")
	print("От 5 до 10 лет  – 15%       От 20 до 25 лет   – 30%")
	print("От 10 до 15 лет – 20%       От 25 и более лет – 40%")
console_picture()

b = a * int(input("Процентная надбавка за выслугу лет: ")) / 100 # умножаю полученный резульат  на процентную надбавку за выслугу лет 
x = a + b 
c = x * 0.7368

def console_picture():
	print(Style.DIM + Fore.RED)
	print("Размер пенсии в зависимости от выслуги лет:")
	print(Style.BRIGHT + Fore.YELLOW)
	print("20 – 50%       24 – 62%       28 – 74%       32 – 85%")
	print("21 – 53%       25 – 65%       29 – 77%")
	print("22 – 56%       26 – 68%       30 – 80%")
	print("23 – 59%       27 – 71%       31 – 83%")
console_picture()

d = c * float(input("Размер пенсии в процентах: ")) / 100
s = d + float (1854.96)

done = False
print(Style.DIM + Fore.RED)
print("Считаю:")
animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
#animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")
time.sleep(2)
done = True

def console_picture():
	print(Style.BRIGHT + Fore.YELLOW)
	print ("Размер выплаты: ", (d), ("₽"))
	print ("С учетом надбавки ветеранам боевых действий: ", (s), ("₽"))
console_picture()
time.sleep(5)
