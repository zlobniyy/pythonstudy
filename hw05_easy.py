# coding: utf-8
__author__ = "Кравченко Степан"

import os
import shutil
import sys

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print( "=" * 20 + "Задание-1" + "=" * 20 )

[os.mkdir( 'dir' + str( i ) ) for i in range( 1, 10 ) if
 not os.path.exists( 'dir' + str( i ) )]  # cоздаем каталоги с проверкой на существование таких же каталогов
[os.removepath.existsdirs( 'dir' + str( i ) ) for i in range( 1, 10 ) if
 os.( 'dir' + str( i ) )]  # удаляем каталоги с проверкой на существование таких каталогов

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print( "=" * 20 + "Задание-2" + "=" * 20 )

curdir = os.path.dirname( __file__ )
[print( nm ) for nm in os.listdir( curdir ) if not os.path.isfile( nm )]

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print( "=" * 20 + "Задание-3" + "=" * 20 )

fl = __file__
if not os.path.exists( fl + '.bak' ):
    shutil.copyfile( fl, fl + '.bak' )
