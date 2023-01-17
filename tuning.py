"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Algorithm Tuner
"""

import numpy as np
import json
from mealpy.tuner import Tuner
from mealpy.evolutionary_based import ES, EP, GA
from mealpy.swarm_based import BeesA, FFA, PSO
from Functions import spring_fitness_function, \
    pressure_fitness_function, \
    spring_get_lb, \
    spring_get_ub, \
    pressure_vessel_get_lb, \
    pressure_vessel_get_ub

#: common

epochs = 100

pop_size = 100

#: problems

problems = {"spring_problem": {"lb": spring_get_lb(),
                               "ub": spring_get_ub(),
                               "minmax": "min",
                               "fit_func": spring_fitness_function,
                               "verbose": False,
                               "name": "Spring Tension Design",
                               "log_to": None},
            "pressure_vessel_problem": {"lb": pressure_vessel_get_lb(),
                                        "ub": pressure_vessel_get_ub(),
                                        "minmax": "min",
                                        "verbose": False,
                                        "fit_func": pressure_fitness_function,
                                        "name": "Pressure Vessel Design",
                                        "log_to": None}}

# algorithms

algorithms = {"solve_ep": EP.LevyEP,
              "solve_es": ES.OriginalES,
              "solve_ga": GA.BaseGA,
              "solve_beesa": BeesA.OriginalBeesA,
              "solve_ffa": FFA.OriginalFFA,
              "solve_pso": PSO.OriginalPSO}

alg_params = {"solve_ep": {"epoch": [epochs],
                           "pop_size": [pop_size],
                           "bout_size": [0.05, 0.06, 0.07, 0.08,
                                         0.09, 0.1, 0.11, 0.12,
                                         0.13, 0.14, 0.15, 0.16,
                                         0.17, 0.18, 0.19, 0.2]},
              "solve_es" :{"epoch": [epochs],
                           "pop_size": [pop_size],
                           "lamda": [0.5, 0.55, 0.6, 0.65, 0.7,
                                     0.75, 0.8, 0.85, 0.9, 0.95,
                                     1.0]},
              "solve_ga": {"epoch": [epochs],
                           "pop_size": [pop_size],
                           "pc": [0.7, 0.75, 0.8,
                                  0.85, 0.9, 0.95],
                           "pm": [0.11, 0.13, 0.15, 0.17, 0.2]},
              "solve_beesa": {"epoch": [epochs],
                              "pop_size": [pop_size],
                              "selected_site_ratio": [0.1, 0.3, 0.5],
                              "elite_site_ratio": [0.1, 0.25, 0.4],
                              "selected_site_bee_ratio": [0.05, 0.1],
                              "elite_site_bee_ratio": [0.25, 0.5, 0.75, 1.0],
                              "dance_radius": [0.025, 0.05, 0.075, 0.1],
                              "dance_reduction": [0.1, 0.5, 0.9, 0.99]},
              "solve_ffa": {"epoch": [epochs],
                            "pop_size": [pop_size],
                            "gamma": [0.001, 0.002, 0.003],
                            "beta_base": [0.5, 1.0, 1.5],
                            "alpha": [0.3, 0.4, 0.5],
                            "alpha_damp": [0.8, 0.9, 0.99],
                            "delta": [0.06, 0.08, 0.1],
                            "exponent": [2]},
              "solve_pso": {"epoch": [epochs],
                            "pop_size": [pop_size],
                            "c1": [1.0, 1.6, 2.0, 2.5, 3.0],
                            "c2": [1.0, 1.6, 2.0, 2.5, 3.0],
                            "w_min": [0.1, 0.2, 0.3, 0.39],
                            "w_max": [0.41, 0.6, 0.8, 1.0, 1.2, 1.5]}
              }

best_parameters = dict()

for problem in problems:
    best_parameters[problem] = dict()
    for solver_name in algorithms:
        print("{:s}-{:s}".format(problem, solver_name))
        model = algorithms[solver_name]()
        params = alg_params[solver_name]
        current_problem = problems[problem]

        tuner = Tuner(model, params)

        ## Get the best model by mean value of all trials
        tuner.execute(problem=current_problem, n_trials=10, mode="parallel", n_workers=4)

        ## Better to save the tunning results to CSV for later usage
        tuner.export_results(f"tuning_params/{problem}_{solver_name}", save_as="csv")

        best_parameters[problem][solver_name] = tuner.best_params

        ## Print out the best pameters
        print(f"Best parameter: {tuner.best_params}")

        ## Print out the best score of the best parameter
        print(f"Best score: {tuner.best_score}")

        ## Print out the algorithm with the best parameter
        print(f"Best Optimizer: {tuner.best_algorithm}")

        ## Now we can even re-train the algorithm with the best parameter by calling resolve() function
        ## Resolve() function will call the solve() function in algorithm with default problem parameter is removed.
        ##    other parameters of solve() function is keeped and can be used.

        best_position, best_fitness = tuner.resolve()
        print(f"Best solution after re-solve: {best_position}")
        print(f"Best fitness after re-solve: {best_fitness}")

with open("results/tuning.json", "w") as f:
    json.dump(best_parameters, f, indent=4)

print(best_parameters)