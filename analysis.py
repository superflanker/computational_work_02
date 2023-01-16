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
        for solver in fit_results[problem]:
            s = min_max_avg_std(fit_results[problem][solver])
            stats[problem]['results'].append([alg_desc[solver],
                                              s['fmin'],
                                              s['favg'],
                                              s['fmean'],
                                              s['fmax'],
                                              s['fstd']])
        stats[problem]['significance'] = friedman_test(fit_results[problem]['solver_ep'],
                                                       fit_results[problem]['solver_es'],
                                                       fit_results[problem]['solver_ga'],
                                                       fit_results[problem]['solver_beesa'],
                                                       fit_results[problem]['solver_ffa'],
                                                       fit_results[problem]['solver_pso'])

    return stats


def min_max_mean_data(best_fits_history):
    stats = dict()
    for problem in best_fits_history:
        stats[problem] = dict()
        stats[problem]['desc'] = problem_desc[problem]
        stats[problem]['results'] = dict()
        stats[problem]['results']['max'] = list()
        stats[problem]['results']['min'] = list()
        stats[problem]['results']['mean'] = list()
        for solver in best_fits_history[problem]:
            history_points = best_fits_history[problem][solver]['population']
            print(json.dump(history_points, indent=4))
            exit()


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

print(fit_results)