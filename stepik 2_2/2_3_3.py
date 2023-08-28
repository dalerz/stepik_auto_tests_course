# Считываем два числа a и b
a = int(input("Введите начало интервала: "))
b = int(input("Введите конец интервала: "))

# Инициализируем переменные для подсчета суммы и количества чисел, делящихся на 3
sum_divisible_by_3 = 0
count_divisible_by_3 = 0

# Проходим по всем числам в интервале [a; b]
for num in range(a, b + 1):
    if num % 3 == 0:
        sum_divisible_by_3 += num
        count_divisible_by_3 += 1

# Вычисляем среднее арифметическое
average = sum_divisible_by_3 / count_divisible_by_3

# Выводим результат
print("Среднее арифметическое чисел, делящихся на 3:", average)
