"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Pressure Vessel Design Problem
optimal value: 5896.94890
x* = (0.780956, 0.386318, 40.433956, 198.504889)
"""

import numpy as np


def pressure_vessel_get_literature_solution():
    return [0.780956, 0.386318, 40.433956, 198.504889]


def pressure_vessel_function(x):
    """
    Function to minimize
    :return: float
    """
    return 0.6224 * x[0] * x[2] * x[3] + \
        1.7781 * x[1] * (x[2] ** 2) + \
        3.1661 * (x[0] ** 2) * x[3] + \
        19.84 * (x[0] ** 2) * x[2]


def p_constraint_g1(x):
    """
    Constraing g1
    :return: float
    """
    return -x[0] + 0.0193 * x[2]


def p_constraint_g2(x):
    """
    Constraint g2
    :return: float
    """
    return -x[1] + 0.00954 * x[2]


def p_constraint_g3(x):
    """
    Constraint g3
    :return: float
    """
    return -np.pi * (x[2] ** 2) * x[3] - (4 / 3) * np.pi * (x[2] ** 3) + 1296000


def p_constraint_g4(x):
    """
    Constraint g4
    :return: float
    """
    return x[3] - 240


def violate(value):
    """
    Constraint Violation
    :param value: constraint function value
    :return: penalty value
    """
    return 0 if value <= 0 else value ** 10


def pressure_vessel_get_lb():
    return [0.75, 0.35, 39.5, 195.0]


def pressure_vessel_get_ub():
    return [0.8, 0.40, 41.0, 205.0]


def pressure_vessel_get_lb_original():
    return [0.0, 0.0, 10.0, 10.0]


def pressure_vessel_get_ub_original():
    return [99.0, 99.0, 200.0, 200.0]


def pressure_fitness_function(solution):
    fx = pressure_vessel_function(solution)

    fx += violate(p_constraint_g1(solution)) + \
          violate(p_constraint_g2(solution)) + \
          violate(p_constraint_g3(solution)) + \
          violate(p_constraint_g4(solution))

    return fx
