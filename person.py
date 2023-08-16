class Person():
    """Модель человека"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Человек создан")

    def sing(self):
        print(self.name + " Поет")

    def dance(self):
        print(self.name + " Танцует")


man = Person("Алекс", 30)
woman = Person("Nata", 28)
# print(man.name)

man.dance()
woman.sing()
#
# choice = input("Завершить операцию? Да / Нет \n").lower()
# if choice == "да":
#     print("\n Операция завершена.")
# elif choice == "нет":
#     print("\n Мне плевать, все равно завершаю.")