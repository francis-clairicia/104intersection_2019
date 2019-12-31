# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 104intersection_2019
## File description:
## cone.py
##

import math
from point import get_point

def intersection_with_cone(point, vector, angle):
    print("Cone with a {} degree angle".format(angle))
    print("Line passing through the point ({}, {}, {})".format(point.x, point.y, point.z), end=" ")
    print("and parallel to the vector ({}, {}, {})".format(vector.x, vector.y, vector.z))
    return None