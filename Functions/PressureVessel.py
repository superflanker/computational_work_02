
"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Pressure Vessel Design Problem
"""

import numpy as np
from sympy import var, exp, cos, pi, euler, sqrt, latex, var, diff, simplify, lambdify
from mealpy.utils.problem import Problem

def pressure_vessel_function():
    """
    Function to minimize
    :return: python function
    """
    x1, x2, x3, x4 = var("x1 x2 x3 x4")
    function = 0.6224 * x1 * x2 * x3 + \
               1.7781 * x2 * (x3 ** 2) + \
               3.1661 * (x1 ** 2) * x4 + \
               19.84 * (x1 ** 2) * x3
    return lambdify([x1, x2, x3, x4], function, "numpy")

def p_constraint_g1():
    """
    Constraing g1
    :return: python function
    """
    x1, x2, x3, x4 = var("x1 x2 x3 x4")
    function = -x1 + 0.0193 * x3
    return lambdify([x1, x2, x3, x4], function, "numpy")

def p_constraint_g2():
    """
    Constraint g2
    :return: python function
    """
    x1, x2, x3, x4 = var("x1 x2 x3 x4")
    function = -x2 + 0.00954 * x3
    return lambdify([x1, x2, x3, x4], function, "numpy")

def p_constraint_g3():
    """
    Constraint g3
    :return: python function
    """
    x1, x2, x3, x4 = var("x1 x2 x3 x4")
    function = -np.pi * (x3 ** 2) * x4 - (4/3) * np.pi * (x3 ** 2) + 1296000
    return lambdify([x1, x2, x3, x4], function, "numpy")

def p_constraint_g4():
    """
    Constraint g4
    :return: python function
    """
    x1, x2, x3, x4 = var("x1 x2 x3 x4")
    function = x4 - 240
    return lambdify([x1, x2, x3, x4], function, "numpy")

def violate(value):
    """
    Constraint Violation
    :param value: constraint function value
    :return: penalty value
    """
    return 0 if value <= 0 else value


def pressure_vessel_get_lb():
    return [0.0, 0.0, 10.0, 10.0]


def pressure_vessel_get_ub():
    return [99.0, 99.0, 200.0, 200.0]


p_func = pressure_vessel_function()

fp_func = lambda x: p_func(*x.flatten())

p_g1 = p_constraint_g1()

fp_g1 = lambda x: p_g1(*x.flatten())

p_g2 = p_constraint_g2()

fp_g2 = lambda x: p_g2(*x.flatten())

p_g3 = p_constraint_g3()

fp_g3 = lambda x: p_g3(*x.flatten())

p_g4 = p_constraint_g4()

fp_g4 = lambda x: p_g4(*x.flatten())

class PressureVessel(Problem):
    """
    Pressure Vessel Design Problem
    """

    def __init__(self, lb, ub, minmax, name="PressureVesselDesign", **kwargs):
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
        fx = fp_func(solution)

        fx += violate(fp_g1(solution)) + \
              violate(fp_g2(solution)) + \
              violate(fp_g3(solution)) + \
              violate(fp_g4(solution))

        return fx
