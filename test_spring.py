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

from Functions import spring_fitness_function, \
    spring_get_lb, \
    spring_get_ub, \
    spring_function, \
    spring_get_literature_solution, \
    s_constraint_g1, \
    s_constraint_g2, \
    s_constraint_g3, \
    s_constraint_g4


spring_default_solution = spring_get_literature_solution()

print(spring_function(spring_default_solution))

print(spring_fitness_function(spring_default_solution))

print(s_constraint_g1(spring_default_solution))
print(s_constraint_g2(spring_default_solution))
print(s_constraint_g3(spring_default_solution))
print(s_constraint_g4(spring_default_solution))