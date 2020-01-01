# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 104intersection_2019
## File description:
## sphere.py
##

from math import sqrt
from point import get_point

def intersection_with_sphere(point, vector, radius):
    print("Sphere of radius {}".format(radius))
    print("Line passing through the point ({}, {}, {})".format(point.x, point.y, point.z), end=" ")
    print("and parallel to the vector ({}, {}, {})".format(vector.x, vector.y, vector.z))
    a = pow(vector.x, 2) + pow(vector.y, 2) + pow(vector.z, 2)
    b = 2 * ((point.x * vector.x) + (point.y * vector.y) + (point.z * vector.z))
    c = pow(point.x, 2) + pow(point.y, 2) + pow(point.z, 2) - pow(radius, 2)
    if a == 0:
        if b == 0:
            return None
        t = -c / b
        return [get_point(point, vector, t)]
    delta = pow(b, 2) - (4 * a * c)
    if delta == 0:
        t = -b / (2 * a)
        return [get_point(point, vector, t)]
    elif delta > 0:
        t1 = (-b + sqrt(delta)) / (2 * a)
        t2 = (-b - sqrt(delta)) / (2 * a)
        return [get_point(point, vector, t1), get_point(point, vector, t2)]
    return None