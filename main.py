#Функция ввода данных
def input_data():
    global age, civil, dis
    try:
        age = int(input("Введите ваш возраст: "))
        civil = input("Вы гражданин страны?(y/n):")
        assert civil == "y" or civil == "Y" or civil == "n" \
               or civil == "N", "Ошибка! Введите y или n"
        dis = input("Вы дисквалифицированы с выборов?(y/n):")
        assert dis == "y" or dis == "Y" or dis == "n" \
               or dis == "N", "Ошибка! Введите y или n"
    except ValueError:
        print("Введите возраст числом!")


#Функция проверки гражданства
def check_civil(civ):
    if civ == "y" or civ == "Y":
        civil_y = True
    else:
        civil_y = False
    return civil_y


#Функция проверки дисквалификации
def check_dis(d):
    if d == "n" or d == "N":
        dis_n = True
    else:
        dis_n = False
    return dis_n


#Функция проверки допуска к выборам
def check_elect():
    if age >= 18 and check_civil(civil) and check_dis(dis):
        print("Вы можете голосовать!")
    else:
        print("Вы не можете голосовать!")


#Основное тело программы
input_data()
check_elect()
