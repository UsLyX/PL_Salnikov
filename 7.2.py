array = [1,2,3,4,5,6,7,8,9,14,16,18,20,22,23]
new_array = []

for i in array:
	if i < 10: new_array.append(0)
	elif i > 20: new_array.append(1)
	else: new_array.append(i)
	
print("Исходный массив: ", *array)
print("Полученный массив: ", *new_array)