# coding utf-8
__author__="Кравченко Степан"

# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: использует метод .format()
k=1
fruits=["яблоко", "банан", "киви", "арбуз","контробандакоал"]
mxlen=max(len(i) for i in fruits)
for i in fruits:
    print('{1}.{0:>10}'.format(i,k))
    k +=1
# не смог понять как сделать выравнивание по самому длинному слову автоматом.
# вычислял длину самого большого слова, но подстановка переменной вместо
# количества символов дает ошибку, так и не победил


# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.
ls1=["выхухоль","арни","андрей","жаба","питон",]
ls2=["степан","вин","арни","жаба","андрей","друзь"]
print(ls1)
print(ls2)
print('+'*50)
ls1copy=ls1
for le2 in ls2:
    for le1 in ls1copy:
        if le1==le2:
            ls1.remove(le1)
        else:
            pass
            #print("le1="+le1+" не похоже на le2="+le2+" - идем дальше")
print(ls1)
print(ls2)


# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
numlist1=[1,2,44,5,346,23,461,3146]
numlist2=[]
for el in numlist1:
    if el%2==0:
        numlist2.append(el/4)
    else:
        numlist2.append(el*2)
print(numlist1)
print(numlist2)