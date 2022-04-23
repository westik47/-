# Калькулятор

import time

from colorama import init
from colorama import Fore, Back, Style
init()

print( Back.GREEN)
print( Fore.BLACK)
what = input("Что делать? (+,-):")
print( Back.CYAN)

a = float( input("Введи первое число: "))
b = float( input("Введи второе число: "))
print( Back.YELLOW)

if what == "+":
	c = a + b
	print("Результат: " + str(c))
elif what == "-":
	c = a - b
	print("Результат: " + str(c))
else:
	print("Выбрана неверная операция!")
	
k=input("нажми любую клавишу")	

time.sleep(15)