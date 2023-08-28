while True:
    try:
        num = int(input("Введите целое число: "))

        if num < 10:
            continue
        elif num > 100:
            break
        else:
            print(num)
    except ValueError:
        print("Ошибка! Введите целое число.")