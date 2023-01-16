"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Analysis Formatter
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json


def latex_results_table(results,
                        desc,
                        problem):

    column_names = ["Algorithm", "Min F", "Mean F", "Median F", "Max F", "StdDev F"]

    df = pd.DataFrame(results,
                      columns=column_names)

    content = df.to_latex(index=False,
                          float_format="%.8f",
                          escape=False,
                          label="function_values:{:s}".format(problem),
                          caption="Statistical Information about function values for {:s}".format(desc))

    return content


def latex_friedman_table(results):
    column_names = ["Problem", "Statistics", "p-value"]

    data = list()

    for problem in results:
        problem_name = results[problem]['desc']
        statistics = results[problem]['significance'][0]
        p_value = results[problem]['significance'][1]
        data.append([problem_name, statistics, p_value])

    df = pd.DataFrame(data,
                      columns=column_names)

    content = df.to_latex(index=False,
                          float_format="%.8f",
                          escape=False,
                          label="friedman_test",
                          caption="Significance Test Using Friedman Chi-Squared Test")

    return content


# statistical data

with open("results/stats.json", "r") as f:
    data = json.load(f)

for problem in data:

    desc = data[problem]['desc']

    results = data[problem]['results']

    content = latex_results_table(results,
                                  desc,
                                  problem)

    with open("latex/includes/{:s}.tex".format(problem), "w") as f:
        f.write(content)

content = latex_friedman_table(data)

with open("latex/includes/friedman_test.tex", "w") as f:
    f.write(content)

# graphics

with open("results/population_history.json", "r") as f:
    population_data = json.load(f)

alg_desc = {"solve_ep": "EP",
            "solve_es": "ES",
            "solve_ga": "GA",
            "solve_beesa": "BeesA",
            "solve_ffa": "FFA",
            "solve_pso": "PSO"}

problem_desc = {'spring_problem': 'Spring Tension Design',
                'pressure_vessel_problem': 'Pressure Vessel Design'}


for problem in population_data:
    for solver in population_data[problem]:
        min = population_data[problem][solver]['min']
        max = population_data[problem][solver]['max']
        mean = population_data[problem][solver]['avg']

        plt.close('all')

        x = np.linspace(1, len(min), len(min))

        plt.plot(x, min, label="Min values")

        plt.plot(x, mean, label="Mean values")

        plt.plot(x, max, label="Max values")

        plt.yscale('log')

        plt.title(alg_desc[solver] + " - " + problem_desc[problem])

        plt.xlabel("Epochs")

        plt.ylabel("Obj. Fun Values")

        plt.legend()

        plt.grid()

        plt.savefig("latex/images/" + problem + "_" + solver + ".jpg", dpi=600)

with open("results/fit_results.json", "r") as f:
    fit_results = json.load(f)

for problem in fit_results:

