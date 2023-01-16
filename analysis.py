"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Result Analysis
"""

import json
import numpy as np
from scipy import stats
from mealpy.utils import io

alg_desc = {"solve_ep": "EP",
            "solve_es": "ES",
            "solve_ga": "GA",
            "solve_beesa": "BeesA",
            "solve_ffa": "FFA",
            "solve_pso": "PSO"}

problem_desc = {'spring_problem': 'Spring Tension Design',
                'pressure_vessel_problem': 'Pressure Vessel Design'}


def fit_results_cleanup(fit_results):
    """
    Results Cleanup
    :param fit_results: raw results
    :return: cleaned results
    """
    new_fit_results = list()
    for node in fit_results:
        new_fit_results.append(node[1])
    return new_fit_results


def population_cleanup(population):
    min_max_mean = {"min": [],
                    "max": [],
                    "avg": []}
    for i in range(0, len(population)):
        pop_data = list()
        for j in range(0, len(population[i])):
            pop_data.append(population[i][j][1][0])
        min_max_mean["min"].append(np.min(pop_data))
        min_max_mean["max"].append(np.max(pop_data))
        min_max_mean["avg"].append(np.mean(pop_data))
    return min_max_mean


def friedman_test(sol0,
                  sol1,
                  sol2,
                  sol3,
                  sol4,
                  sol5):
    """
    Executes Friedman Qui-Squared Similarity Test
    :param sol0: solutions for algorithm 0
    :param sol1: solutions for algorithm 1
    :param sol2: solutions for algorithm 2
    :param sol3: solutions for algorithm 3
    :param sol4: solutions for algorithm 4
    :param sol5: solutions for algorithm 5
    :return: statistics, pvalue
    """
    statistics, pvalue = stats.friedmanchisquare(sol0,
                                                 sol1,
                                                 sol2,
                                                 sol3,
                                                 sol4,
                                                 sol5)
    return statistics, pvalue


def ordinary_statistics(fit_results):
    """
    Computes ordinary statistics for all the final results
    :param fit_results: the final results for each problerm-algorithm pair
    :return: dict the stats compiled by problem
    """

    def min_max_avg_std(data):
        """
        Computes min, max, avg and std from results
        :param data: the results data
        :return: min, max, avg, std, first_quantile and third_quantile values
        """
        fmin = 0
        fmax = 0
        favg = 0
        fmedian = 0
        fstd = 0

        if len(data) > 0:
            fmin = float(np.min(data))
            fmax = float(np.max(data))
            favg = float(np.mean(data))
            fmedian = float(np.median(data))
            fstd = float(np.std(data))

        return {"fmin": fmin,
                "fmax": fmax,
                "favg": favg,
                "fmedian": fmedian,
                "fstd": fstd}

    stats = dict()

    for problem in fit_results:
        stats[problem] = dict()
        stats[problem]['desc'] = problem_desc[problem]
        stats[problem]['results'] = list()
        solver_data = dict()
        for solver in fit_results[problem]:
            data = fit_results_cleanup(fit_results[problem][solver])
            solver_data[solver] = data
            s = min_max_avg_std(data)
            stats[problem]['results'].append([alg_desc[solver],
                                              s['fmin'],
                                              s['favg'],
                                              s['fmedian'],
                                              s['fmax'],
                                              s['fstd']])

        stats[problem]['significance'] = friedman_test(solver_data['solve_ep'],
                                                       solver_data['solve_es'],
                                                       solver_data['solve_ga'],
                                                       solver_data['solve_beesa'],
                                                       solver_data['solve_ffa'],
                                                       solver_data['solve_pso'])

        with open("results/" + problem + "_fit_results.json", "w") as f:
            json.dump(solver_data, f, indent=4)

    return stats


# collecting results
with open("results/best_fits.json", "r") as f:
    best_fits = json.load(f)

with open("results/fit_results.json", "r") as f:
    fit_results = json.load(f)

best_fits_history = dict()

for problem in problem_desc:
    best_fits_history[problem] = dict()
    for solver in alg_desc:
        filename = "results/best_" + problem + "_" + solver
        model = io.load_model(filename)
        best_fits_history[problem][solver] = model

stats = ordinary_statistics(fit_results)

with open("results/stats.json", "w") as f:
    json.dump(stats, f, indent=4)


population_stats = dict()

for problem in best_fits_history:
    population_stats[problem] = dict()
    for solver in best_fits_history[problem]:
        population_stats[problem][solver] = population_cleanup(best_fits_history[problem][solver].history.list_population)

with open("results/population_history.json", "w") as f:
    json.dump(population_stats, f, indent=4)
