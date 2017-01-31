# coding: utf-8
__author__ = "Кравченко Степан"
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math
print( "=" * 20 + "Задание-1" + "=" * 20 )


def my_round(number, ndigits):
    '''Это самопальная функция округления числа.'''
    lsch = str( number ).split( "." )
    ch1 = lsch[0]
    ch2 = lsch[1]
    num2 = list( map( int, str( ch2 ) ) )
    num1 = list( map( int, str( ch1 ) ) )
    num2copy = num2
    for i in range( len( num2copy ) - 1, ndigits, -1 ):
        if num2[i] > 4:
            # num2[i-1] = num2[i-1]+1
            num2[i - 1] += 1
            num2[i] = 0
        num2.pop( i )
    # print(num2)
    if num2[0] > 4:
        num1[0] += 1
    print( number )
    print( "".join( map( str, num1 ) ) + "." + "".join( map( str, num2 ) ) )


my_round( 2.1234567, 5 )

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print( "=" * 20 + "Задание-2" + "=" * 20 )


def lucky_ticket(ticket_number):
    '''Функция определения счастливого билетика'''

    part1 = list( map( int, str( ticket_number )[:8] ) )
    part2 = list( map( int, str( ticket_number )[8:] ) )
    if sum( part1 ) == sum( part2 ):
        return 1
    else:
        return 0


lucky_ticket( 1234567890123456 )
lucky_ticket( 1212121212121212 )
