
# 1. Прямоугольник

import math

x = None
y = None

point = (x, y)
point1 = (1, 2)
point2 = (3, 4)
point3 = (5, 6)

rect1 = [point, point1]
point = {'x':0, 'y':0}
rect = {'x':1, 'y':2, 'w':13, 'h':5}
circle = {'x':1, 'y':2, 'r':5}


class Point:
    ''' Класс точек
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    """Документация for Figure"""
    def __init__(self, x, y):
        self.x = x
        self.y = y        
        
    def move(figure, point):
        figure.x = point.x
        figure.y = point.y 

    def square(self):
        pass
        print('У абстрактной фигуры нет площади')     


                                  # - для Python 2
class Rectangle(Figure):          # (object) - для Python 2
    def __init__(self, x, y, w, h):
        super().__init__(x, y)    # super(Rectangle, self).__init__(x, y)
        self.w = w
        self.h = h
        self._zorro = 'xxx'
        self.__zzz = 'protected'

    @property    
    def square(self):
        return self.w * self.h

    @property    
    def perim(rect):
        return 2 * (rect.w + rect.h)

    def __str__(self):
        return 'Прямоугольник ({x},{y}): w={width}, h={height}'.format(x=self.x,
         y=self.y, width=self.w, height=self.h)



class Circle(Figure):        # (object) - для Python 2
    def __init__(self, r):
        super().__init__(0, 0)
        self.r = r

    @property  
    def square(self):
        return math.pi * (self.r ** 2)

    @property  
    def length(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return 'Круг ({x},{y}): r={radius}'.format(x=self.x,
         y=self.y, radius=self.r)        



class Zuzuka(Figure):        # (object) - для Python 2
    def __init__(self, x, y, zzz):
        super().__init__(x, y)
        self.zzz = zzz


# z = Zuzuka(1, 2, 'super')        
# z.square()





rect = Rectangle(0, 0, 7, 5)
circle = Circle(7)

print(rect)
print(circle)








def think(brain, koviryat=False, finger=1, nose=0):
    if koviryat:
        finger, nose = 0, 1
    brain = 2 ** 10    


# 2. Площадь
def square_rect(rect):
    return rect['w'] * rect['h']


# 2. Площадь круга
def square_circle(rect):
    return rect['w'] * rect['h']


# 3. Периметр    
def perim(rect):
    return 2 * (rect['w'] + rect['h'])


# 4. Переместить
def move(figure, point):
    figure['x'] = point['x']
    figure['y'] = point['y']