#coding utf-8
__author__="Кравченко Степан"

# Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
# Определить координату y, точки с заданной координатой x

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
decomp=equation.split()
#print(decomp)
xexp=int((decomp[2].split("x"))[0])
#print(xexp)
if decomp[4]=="+":
    y = xexp * x + float(decomp[-1])
else:
    y = xexp * x - float(decomp[-1]) #не стал рассматривать другие операции кроме "минуса", и так не красиво
    # но ничего лучше сходу не придумал как распознать и подставить арифметическое действие
print(y)
print("="*79)
# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'. Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

dmc={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
dmn={1:"январе",2:"феврале",3:"марте",4:"апреле",5:"мае",6:"июне",
    7:"июле",8:"августе",9:"сентябре",10:"октябре",11:"ноябре",12:"декабре"}
date = '31.11.1999'
date_check=date.split(".")
day=int(date_check[0])
month=int(date_check[1])
year=int(date_check[2])
print(date)
if year not in range(1,10000):
    print("Год",year,"введен неверно.")
else:
    if month not in range(1,13):
        print(month)
        print("В году нет '"+str(month)+"-го' месяца")
        month_name = None
    else:
        month_name = dmn[month]
        if day not in range(1,dmc[month]+1):
            print("Нет дня",day,"в",month_name)
        else:
            print("Дата",date,"введена корректно")
print("="*79)
# Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа,
# на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача: нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

############# не сделано ##############

tflat=140
floors=0
flat_numb=0
flats_on_floor=0
tf=0
f=0
ind=0
floors_numb=0
tfloor=0
#z:=0
while tflat >= flat_numb:
    f += 1
    print("f",f)
    floors_numb += f
    flat_numb += f**2
    tf=flat_numb

for z in range(1,f+1):
    if flat_numb-f*z<tf:
            tfloor=floors_numb
    else:
        pass
    print(z)
    print(tfloor)



    print( "floors_numb", floors_numb )
    print( "flat_numb", flat_numb )
    print("-"*15)
print("tfloor",tfloor)