
"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Spring Design Problem
"""

import numpy as np
from sympy import var, exp, cos, pi, euler, sqrt, latex, var, diff, simplify, lambdify
from mealpy.utils.problem import Problem

def spring_function():
    """
    Function to minimize
    :return: python function
    """
    x1, x2, x3 = var("x1 x2 x3")
    function = (x3 + 2) * x2 * (x1 ** 2)
    return lambdify([x1, x2, x3], function, "numpy")

def s_constraint_g1():
    """
    Constraing g1
    :return: python function
    """
    x1, x2, x3 = var("x1 x2 x3")
    function = 1 - ((x2 ** 3) * x3)/(71785.0 * (x1 ** 4))
    return lambdify([x1, x2, x3], function, "numpy")

def s_constraint_g2():
    """
    Constraint g2
    :return: python function
    """
    x1, x2, x3 = var("x1 x2 x3")
    function = (4 * (x2 ** 2) - x1 * x2)/(12566 * (x2 * (x1 ** 3) - x1 ** 4)) + 1/(5108 * (x1 ** 2)) - 1
    return lambdify([x1, x2, x3], function, "numpy")

def s_constraint_g3():
    """
    Constraint g3
    :return: python function
    """
    x1, x2, x3 = var("x1 x2 x3")
    function = 1 - (140.45 * x1)/((x2 ** 2) * x3)
    return lambdify([x1, x2, x3], function, "numpy")

def s_constraint_g4():
    """
    Constraint g4
    :return: python function
    """
    x1, x2, x3 = var("x1 x2 x3")
    function = (x1 + x2)/1.5 - 1
    return lambdify([x1, x2, x3], function, "numpy")

def violate(value):
    """
    Constraint Violation
    :param value: constraint function value
    :return: penalty value
    """
    return 0 if value <= 0 else value ** 2


def spring_get_lb():
    return [0.05, 0.25, 2.0]


def spring_get_ub():
    return [2.0, 1.3, 15.0]

"""
Lambda functions => mappings
"""

s_func = spring_function()

fs_func = lambda x: s_func(*x.flatten())

s_g1 = s_constraint_g1()

fs_g1 = lambda x: s_g1(*x.flatten())

s_g2 = s_constraint_g2()

fs_g2 = lambda x: s_g1(*x.flatten())

s_g3 = s_constraint_g3()

fs_g3 = lambda x: s_g3(*x.flatten())

s_g4 = s_constraint_g4()

fs_g4 = lambda x: s_g4(*x.flatten())

def spring_fitness_function(solution):
    fx = fs_func(solution)

    fx += violate(fs_g1(solution)) + \
          violate(fs_g2(solution)) + \
          violate(fs_g3(solution)) + \
          violate(fs_g4(solution))

    return fx

'''
class Spring(Problem):
    """
    Spring Tension Design Problem
    """

    def __init__(self, lb, ub, minmax, name="SpringTensionDesign", **kwargs):
        """
        Constructor
        :param lb: lower bound
        :param ub: upper bound
        :param minmax: max/min problem
        :param name: Problem Name
        :param kwargs: extra args
        """
        super().__init__(lb, ub, minmax, **kwargs)
        self.name = name

    def fit_func(self, solution):
        fx = fs_func(solution)

        fx += violate(fs_g1(solution)) + \
              violate(fs_g2(solution)) + \
              violate(fs_g3(solution)) + \
              violate(fs_g4(solution))

        return fx'''
