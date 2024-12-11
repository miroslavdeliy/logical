#Ввод данных и проверка корректности ввода возраста
try:
    age = int(input("Введите ваш возраст: "))
    civil = input("Вы гражданин страны?(y/n):")
    dis = input("Вы дисквалифицированы с выборов?(y/n):")
except ValueError:
    print("Введите возраст числом!")

#Проврка корректности ввода гражданства
if civil == "y" or civil == "Y":
    civil_y = True
elif civil == "n" or civil == "N":
    civil_y = False
else:
    print("Ошибка! Введите y или n")

#Проверка корректности ввода дисквалификации
if dis == "n" or dis == "N":
    dis_n = True
elif dis == "y" or dis == "Y":
    dis_n = False
else:
    print("Ошибка! Введите y или n")

#Проверка допуска к выборам
if age >= 18 and civil_y and dis_n:
    print("Вы можете голосовать!")
else:
    print("Вы не можете голосовать!")
