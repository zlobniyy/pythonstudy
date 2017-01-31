# coding: utf-8
__author__ = "Кравченко Степан"

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print( "=" * 20 + "Задание-1" + "=" * 20 )


def fibonacci(n, m):
    '''функция вычисляет ряд Фибоначчи до заданного порядка'''

    fib = [0, 1]
    while len( fib ) < m:
        fib.append( fib[-2] + fib[-1] )
    print( fib[n:] )


fibonacci( 8, 13 )

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print( "=" * 20 + "Задание-2" + "=" * 20 )


def sort_to_max(origin_list):
    ''' функция сортировки списка по убыванию'''

    k = 1
    while k < len( origin_list ):
        for i in range( len( origin_list ) - k ):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        k += 1
    print( origin_list )


sort_to_max( [2, 10, -12, 2.5, 20, -11, 4, 4, 0] )

# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print( "=" * 20 + "Задание-3" + "=" * 20 )
print( "=" * 20 + "не сделано" + "=" * 20 )


def my_filter():
    '''функция реализующая фильтр'''
    pass


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print( "=" * 20 + "Задание-4" + "=" * 20 )
print( "=" * 20 + "не сделано" + "=" * 20 )
import math


def dots_to_para(x1, y1, x2, y2, x3, y3, x4, y4):
    '''функция проверки точек на вершины параллелограмма'''
    coords = [x1, y1, x2, y2, x3, y3, x4, y4]

    def dst_btwn_dots(dx1, dy1, dx2, dy2):
        '''функция вычисляет расстояние между двумя точками'''
        dbd = math.sqrt( (dx1 - dx2) ** 2 + (dy1 - dy2) ** 2 )
        return dbd

    print( "ответ:" )


dots_to_para( 4, 8, 2, 3, 4, 12, 10, 3 )
