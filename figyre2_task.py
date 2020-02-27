from abc import  abstractmethod
import os

import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint

class Figure:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @abstractmethod
    def perimeter(self):
        ...

    def square(self):
        ...
    @property
    def width(self):
        return 0.0

    @property
    def height(self):
        return 0.0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,x):
        if not isinstance(x,int):
            raise TypeError
        return self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,y):
        if not isinstance(x, int):
            raise TypeError
        return self._y

class Rectangle(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        # self.__x = x
        # self.__y = y
        super().__init__(x,y)
        self.width = w
        self.height = h

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width,int):
            raise TypeError
        self.__width=width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError
        self.__height = height

    def perimeter(self):
        return 2 * (self.w + self.h)

    def square(self):
        return self.w * self.h

    def width(self):
        return self.w

    def height(self):
        return self.h
class Ellipse(Rectangle):
    def __init__(self, x=0, y=0 ): #w=0, h=0
        super().__init__(x, y)
        self.width = 2 * a
        self.height = 2 * b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError
        self.__height = height
class CloseFigure(Figure):
    def __init__(self,*args):
        # нужно получить из списка значение x и y args ->...->self.d
        self.d = [{'x':x0, 'y':y0},
                  {'x':x1, 'y':y1}]
        # for x,y in args:





