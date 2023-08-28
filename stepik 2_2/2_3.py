# Ввод четырех чисел a, b, c, d
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Вывод заголовочной строки
print('\t', end='')
for j in range(c, d + 1):
    print(j, end='\t')
print()

# Вывод таблицы умножения
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()
