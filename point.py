# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 104intersection_2019
## File description:
## point.py
##

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Vector(Point):

    def __init__(self, x, y, z):
        Point.__init__(self, x, y, z)


def get_point(point, vector, t):
    x = point.x + (t * vector.x)
    y = point.y + (t * vector.y)
    z = point.z + (t * vector.z)
    return Point(x, y, z)