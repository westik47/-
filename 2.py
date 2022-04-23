number = 23
running = True

while running:
	guess = int(input("Введите целое число: "))

	if guess == number:
		print("Поздравляю, вы угадали!")
		running = False
	elif guess < number:
		print("Заданное чило немного больше введенного!")	
	else:
		print("Заданнное число немного меньше введенного!")
else:
	print("Цилк Wile закончен!")
	# Здесь можете выполнить всё что вам ещё нужно
print("Завершение!")			
