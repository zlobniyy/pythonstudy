# coding: utf-8
__author__ = "Кравченко Степан"

# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл из easy.py
import os

print( "=" * 20 + "Задание-1" + "=" * 20 )
name = input( "Введите Ваше имя: " )
print( "Здравствуйте, " + name + "." )
choise=None
while choise != 'q':
    print("-"*79)
    print( "1. Перейти в папку" )
    print( "2. Просмотреть содержимое текущей папки" )
    print( "3. Удалить папку" )
    print( "4. Создать папку" )
    print( "q. выйти из программы" )
    choise = input( "Выберете действие: " )
    if choise == '1':
        tdir = input("Введите путь до папки: ")
        if os.path.exists(tdir):
            os.chdir(tdir)
            print( "Текущий каталог: " + os.getcwd( ) )
        else:
            print("Такого каталога не существует.")
    elif choise =='2':
        curdir = os.path.dirname( '.' )
        print( "Содержимое папки: " + os.getcwd( ))
        [print( nm ) for nm in os.listdir( "." )]
    elif choise=='3':
        tdir = input( "Введите путь до папки: " )
        if os.path.exists( tdir ):
            os.removedirs( tdir )
        else:
            print("Такого каталога не сужествует.")
    elif choise=='4':
        tdir = input( "Введите путь до папки: " )
        if not os.path.exists( tdir ):
            os.mkdir( tdir )
        else:
            print( "Такой каталог уже сужествует." )
    elif choise == 'q':
        pass
    else:
        print("Введите корректное значение.")
