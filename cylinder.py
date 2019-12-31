# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 104intersection_2019
## File description:
## cylinder.py
##

import math
from point import get_point

def determine_solution(point, vector, radius):
    a = pow(vector.x, 2) + pow(vector.y, 2)
    b = 2 * point.x * vector.x + 2 * point.y * vector.y  
    c = pow(point.x, 2) + pow(point.y, 2) - pow(radius, 2)
    solution = list()

    if a == 0:
        if b == 0:
            return None
        t = -c / b
        solution.append(get_point(point, vector, t))
    else:
        delta = pow(b, 2) - 4 * a * c

        if (delta > 0):
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            solution.append(get_point(point, vector, x1))
            solution.append(get_point(point, vector, x2))
        elif (delta == 0):
            x = -b / (2 * a)
            solution.append(get_point(point, vector, x))
        else: 
            return None
    return solution

def intersection_with_cylinder(point, vector, radius):
    print("Cylinder of radius {}".format(radius))
    print("Line passing through the point ({}, {}, {})".format(point.x, point.y, point.z), end=" ")
    print("and parallel to the vector ({}, {}, {})".format(vector.x, vector.y, vector.z))
    solution = determine_solution(point, vector, radius)
    return solution
