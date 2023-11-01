numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_index = numbers.index(None)
s = sum(numbers[:missing_index ]) + sum(numbers[missing_index +1:])
numbers[missing_index] = s

print("Измененный список:", numbers)
