"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Spring Design Problem
optimal value: 0.012665
x∗ = (0.051690, 0.356750, 11.287126)
"""

def spring_get_literature_solution():
    return [0.051690, 0.356750, 11.287126]

def spring_function(x):
    """
    Function to minimize
    :return: float
    """
    return (x[0] ** 2) * x[1] * (2 + x[2])


def s_constraint_g1(x):
    """
    Constraing g1
    :return: float
    """
    return 1 - (((x[1] ** 3) * x[2]) / (71785.0 * (x[0] ** 4)))


def s_constraint_g2(x):
    """
    Constraint g2
    :return: float
    """
    return ((4 * (x[1] ** 2) - x[0] * x[1]) / (12566.0 * ((x[0] ** 3) * x[1] - x[0] ** 4)))+ \
        (1 / (5108.0 * (x[0] ** 2))) - 1.0


def s_constraint_g3(x):
    """
    Constraint g3
    :return: float
    """
    return 1 - ((140.45 * x[0]) / ((x[1] ** 2) * x[2]))


def s_constraint_g4(x):
    """
    Constraint g4
    :return: python function
    """
    value = ((x[0] + x[1]) / 1.5) - 1
    return value


def violate(value):
    """
    Constraint Violation
    :param value: constraint function value
    :return: penalty value
    """
    return 0 if value <= 0 else value ** 2


def spring_get_lb():
    """
    Lower bound
    :return: array
    """
    return [0.05, 0.25, 2.0]


def spring_get_ub():
    """
    Upper bound
    :return: array
    """
    return [2.0, 1.3, 15.0]


def spring_fitness_function(solution):
    fx = spring_function(solution)

    fx += violate(s_constraint_g1(solution)) + \
          violate(s_constraint_g2(solution)) + \
          violate(s_constraint_g3(solution)) + \
          violate(s_constraint_g4(solution))

    return fx
