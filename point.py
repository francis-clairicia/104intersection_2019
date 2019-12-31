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

    @classmethod
    def from_two_points(cls, point_a, point_b):
        x = point_b.x - point_a.x
        y = point_b.y - point_a.y
        z = point_b.z - point_a.z
        return cls(x, y, z)

def get_point(point, vector, t):
    x = point.x + (t * vector.x)
    y = point.y + (t * vector.y)
    z = point.z + (t * vector.z)
    return Point(x, y, z)