"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Test Spring Functions
"""

import json
import numpy as np

from mealpy.evolutionary_based import ES, EP, GA
from mealpy.swarm_based import BeesA, FFA, PSO
from mealpy.utils import io

from Functions import pressure_fitness_function, \
    pressure_vessel_get_lb, \
    pressure_vessel_get_ub, \
    pressure_vessel_function, \
    pressure_vessel_get_literature_solution, \
    p_constraint_g1, \
    p_constraint_g2, \
    p_constraint_g3, \
    p_constraint_g4


pressure_vessel_default_solution = pressure_vessel_get_literature_solution()

print(pressure_vessel_function(pressure_vessel_default_solution))

print(pressure_fitness_function(pressure_vessel_default_solution))

print(p_constraint_g1(pressure_vessel_default_solution))
print(p_constraint_g2(pressure_vessel_default_solution))
print(p_constraint_g3(pressure_vessel_default_solution))
print(p_constraint_g4(pressure_vessel_default_solution))