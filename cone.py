# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 104intersection_2019
## File description:
## cone.py
##

from sys import float_info
from math import sqrt, tan, radians
from point import get_point

def intersection_with_cone(point, vector, angle):
    print("Cone with a {} degree angle".format(angle))
    print("Line passing through the point ({}, {}, {})".format(point.x, point.y, point.z), end=" ")
    print("and parallel to the vector ({}, {}, {})".format(vector.x, vector.y, vector.z))
    tan_angle = tan(radians(angle))
    a = pow(vector.x, 2) + pow(vector.y, 2) - (pow(vector.z, 2) * pow(tan_angle, 2))
    b = 2 * ((point.x * vector.x) + (point.y * vector.y) - ((point.z * vector.z) * pow(tan_angle, 2)))
    c = pow(point.x, 2) + pow(point.y, 2) - (pow(point.z, 2) * pow(tan_angle, 2))
    if round(a, 5) == 0.0:
        if round(b, 5) == 0 or round(c, 5):
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