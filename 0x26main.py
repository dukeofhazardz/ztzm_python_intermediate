numbers = [3, 4, 7, 10, 15, 18, 21]
even_numbers = (num for num in numbers if num % 2 == 0)

for even in even_numbers:
    print(even)
