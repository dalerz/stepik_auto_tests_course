pin = 1234
print("Введите pin")
user_pin = int(input())

if pin == user_pin:
    print("Какую сумму")

else:
    print("Ошибка осталось 2 попытки")
    user_pin = int(input())
    if pin == user_pin:
        print("Какую сумму")

    else:
        print("Ошибка осталось 1 попытки")
        user_pin = int(input())
        if pin == user_pin:
            print("Какую сумму")
        else:
            print("Ошибкаб осталось 0 попытки")