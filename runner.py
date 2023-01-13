"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Optimization Runner
"""

import json
import numpy as np
from mealpy.evolutionary_based import ES, EP, GA
from mealpy.swarm_based import BeesA, FFA, PSO
from Functions import spring_fitness_function, \
    pressure_fitness_function, \
    spring_get_lb, \
    spring_get_ub, \
    pressure_vessel_get_lb, \
    pressure_vessel_get_ub

s_lb = spring_get_lb()

s_ub = spring_get_ub()

p_lb = pressure_vessel_get_lb()

p_ub = pressure_vessel_get_ub()

# common

epochs = 50

pop_size = 100

runs = 30

# problems

problems = {"spring_problem": {"lb": spring_get_lb(),
                               "ub": spring_get_ub(),
                               "minmax": "min",
                               "fit_func": spring_fitness_function,
                               "verbose": False,
                               "name": "Spring Tension Design",
                               "save_population": True,
                               "log_to": None},
            "pressure_vessel_problem": {"lb": pressure_vessel_get_lb(),
                                        "ub": pressure_vessel_get_ub(),
                                        "minmax": "min",
                                        "verbose": False,
                                        "fit_func": pressure_fitness_function,
                                        "name": "Pressure Vessel Design",
                                        "save_population": True,
                                        "log_to": None}}

# algorithm mapping

algorithms = {"solve_ep": EP.LevyEP,
              "solve_es": ES.OriginalES,
              "solve_ga": GA.BaseGA,
              "solve_beesa": BeesA.OriginalBeesA,
              "solve_ffa": FFA.OriginalFFA,
              "solve_pso": PSO.OriginalPSO}

# tuning parameters - given by tuning.py

with open("results/tuning.json", "r") as f:
    alg_params = json.load(f)

# storage variables

best_fits = {"spring_problem": {"solve_ep": 1e6,
                                "solve_es": 1e6,
                                "solve_ga": 1e6,
                                "solve_beesa": 1e6,
                                "solve_ffa": 1e6,
                                "solve_pso": 1e6},
             "pressure_vessel_problem": {"solve_ep": 1e6,
                                         "solve_es": 1e6,
                                         "solve_ga": 1e6,
                                         "solve_beesa": 1e6,
                                         "solve_ffa": 1e6,
                                         "solve_pso": 1e6}}


best_fits_history = {"spring_problem": {"solve_ep": [],
                                        "solve_es": [],
                                        "solve_ga": [],
                                        "solve_beesa": [],
                                        "solve_ffa": [],
                                        "solve_pso": []},
                     "pressure_vessel_problem": {"solve_ep": [],
                                                 "solve_es": [],
                                                 "solve_ga": [],
                                                 "solve_beesa": [],
                                                 "solve_ffa": [],
                                                 "solve_pso": []}}

fit_results = {"spring_problem": {"solve_ep": [],
                                  "solve_es": [],
                                  "solve_ga": [],
                                  "solve_beesa": [],
                                  "solve_ffa": [],
                                  "solve_pso": []},
               "pressure_vessel_problem": {"solve_ep": [],
                                           "solve_es": [],
                                           "solve_ga": [],
                                           "solve_beesa": [],
                                           "solve_ffa": [],
                                           "solve_pso": []}}

# at last, the optimization run

for seed in range(1, runs + 1):
    print("Seed: {:d}".format(seed))
    for problem in alg_params:
        current_problem = problems[problem]
        print("Problem: {:s}".format(problem))
        for solver_name in algorithms:
            np.random.seed(seed)
            params = alg_params[problem][solver_name]
            model = algorithms[solver_name](**params)
            best_position, best_fitness = model.solve(current_problem)
            fit_results[problem][solver_name].append([best_position.tolist(), best_fitness])
            if best_fitness <= best_fits[problem][solver_name]:
                best_fits[problem][solver_name] = best_fitness
                best_fits_history[problem][solver_name] = model.history.list_population

# saving best fits
with open("results/best_fits.json", "w") as f:
    json.dump(best_fits, f, indent=4)

# saving fit results
with open("results/fit_results.json", "w") as f:
    json.dump(fit_results, f, indent=4)

with open("results/best_fits_history.pkl", "w") as f:

    np.dump(f, best_fits_history)