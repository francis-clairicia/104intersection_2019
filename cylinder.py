# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 104intersection_2019
## File description:
## cylinder.py
##

import math
from point import Point, Vector

def intersection_with_cylinder(point, vector, radius):
    print("Cylinder of radius {}".format(radius))
    print("Line passing through the point ({}, {}, {})".format(point.x, point.y, point.z), end=" ")
    print("and parallel to the vector ({}, {}, {})".format(vector.x, vector.y, vector.z))
    return None