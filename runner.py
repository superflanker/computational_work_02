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
from mealpy.utils import io

from Functions import spring_fitness_function, \
    pressure_fitness_function, \
    spring_get_lb, \
    spring_get_ub, \
    pressure_vessel_get_lb, \
    pressure_vessel_get_ub


def create_starting_positions(rseed,
                              n_dims,
                              pop_size,
                              lb,
                              ub):
    """
    Initial population
    :param rseed: random seed
    :param n_dims: problem dimention
    :param pop_size: population size
    :param lb: lower bound
    :param ub: upper bound
    :return: initial population
    """
    rng = np.random.default_rng(rseed)
    random_extractions = rng.random((pop_size, n_dims))
    for i in range(0, n_dims):
        random_extractions[:, i] = (ub[i] - lb[i]) * random_extractions[:, i] + lb[i]
    return random_extractions


# common
epochs = 100

pop_size = 100

runs = 100

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

n_dims = {"spring_problem": 3,
          "pressure_vessel_problem": 4}

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

        initial_positions = create_starting_positions(seed,
                                                      n_dims[problem],
                                                      pop_size,
                                                      current_problem["lb"],
                                                      current_problem["ub"])

        for solver_name in algorithms:
            print(solver_name)
            np.random.seed(seed)
            params = alg_params[problem][solver_name]
            model = algorithms[solver_name](**params)
            best_position, best_fitness = model.solve(current_problem,
                                                      starting_positions=initial_positions)

            fit_results[problem][solver_name].append([best_position.tolist(),
                                                      best_fitness])
            if best_fitness <= best_fits[problem][solver_name]:
                best_fits[problem][solver_name] = float(best_fitness)
                best_fits_history[problem][solver_name] = model

# saving best fits
with open("results/best_fits.json", "w") as f:
    json.dump(best_fits, f, indent=4)

# saving fit results
with open("results/fit_results.json", "w") as f:
    json.dump(fit_results, f, indent=4)

for problem in best_fits_history:
    for solver in best_fits_history[problem]:
        model = best_fits_history[problem][solver]
        filename = "results/best_" + problem + "_" + solver
        io.save_model(model, filename)
