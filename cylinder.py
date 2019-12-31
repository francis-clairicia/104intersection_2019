# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 104intersection_2019
## File description:
## cylinder.py
##

import math
from point import Point, Vector

def dertimine_solution(point, vector, radius)
    a = pow(vector.x, 2) + pow(vector.y, 2)
    b = 2 * point.x * vector.x + 2 * point.y * vector.y  
    c = pow(point.x, 2) + pow(point.y, 2) - pow(radius, 2)

    t = pow(b, 2) * -1 - 4 * a * c

    solution = list();
    if (t > 0):
        x1 = (-b * sqrt(t)) / 2 * a 
        x2 = (-b * -sqrt(t)) / 2 * a 
        solution = list.append(get_point(point, vector, x1))
        solution = list.append(get_point(point, vector, x2))
    elif (t == 0):
        x = -b / (2 * a)
        solution = list.append(get_point(point, vextor, x))
    else: 
        return None
    return solution

def intersection_with_cylinder(point, vector, radius):
    soluion = dertermine_solution(point, vectot, radius)
    print("Cylinder of radius {}".format(radius))
    print("Line passing through the point ({}, {}, {})".format(point.x, point.y, point.z), end=" ")
    print("and parallel to the vector ({}, {}, {})".format(vector.x, vector.y, vector.z))
    return None
