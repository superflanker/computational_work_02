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
import matplotlib.pyplot as plt
import json


def latex_results_table(results,
                        desc,
                        problem):

    column_names = ["Algorithm",
                    "Min F",
                    "Mean F",
                    "Median F",
                    "Max F",
                    "StdDev F"]

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
                'pressure_vessel_problem': 'Pressure Vessel Design',
                'pressure_vessel_problem_original': 'Pressure Vessel Design (Original)'}


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

        plt.ylabel("Obj. Fun Values(log)")

        plt.legend()

        plt.grid()

        plt.savefig("latex/images/" + problem + "_" + solver + ".png", dpi=600)

        content = """\\begin{figure}[H]
        \\centering
        \\caption{Convergence lines for """ + alg_desc[solver] + " - " + problem_desc[problem] + """}
        \\label{fig:""" + problem + "_" + solver + """}
        \\includegraphics[scale=0.5]{images/""" + problem + "_" + solver +  """.png}
        \\end{figure}
        """
        with open("latex/includes/" + problem + "_" + solver + ".tex", "w") as f:
            f.write(content)

with open("results/spring_problem_fit_results.json", "r") as f:
    fit_results = json.load(f)

#: spring problem boxplots

fit_keys = [alg_desc[x] for x in fit_results]

fit_values = fit_results.values()

plt.close('all')

plt.boxplot(fit_values, labels=fit_keys)

plt.title("Spring Tension Design - Boxplot")

plt.savefig("latex/images/spring_problem_boxplot.png", dpi=600)

content = """\\begin{figure}[H]
\\centering
\\caption{Boxplot for Spring Tension Design}
\\label{fig:spring_tension_design_boxplot}
\\includegraphics[scale=0.5]{images/spring_problem_boxplot.png}
\\end{figure}
"""
with open("latex/includes/spring_problem_boxplot.tex", "w") as f:
    f.write(content)

with open("results/pressure_vessel_problem_fit_results.json", "r") as f:
    fit_results = json.load(f)

#: spring problem boxplots

fit_keys = [alg_desc[x] for x in fit_results]

fit_values = fit_results.values()

plt.close('all')

plt.boxplot(fit_values, labels=fit_keys)

plt.title("Pressure Vessel Design - Boxplot")

plt.savefig("latex/images/pressure_vessel_problem_boxplot.png", dpi=600)

content = """\\begin{figure}[H]
\\centering
\\caption{Boxplot for Pressure Vessel Design}
\\label{fig:pressure_vessel_design_boxplot}
\\includegraphics[scale=0.5]{images/pressure_vessel_problem_boxplot.png}
\\end{figure}
"""
with open("latex/includes/pressure_vessel_problem_boxplot.tex", "w") as f:
    f.write(content)


with open("results/pressure_vessel_problem_original_fit_results.json", "r") as f:
    fit_results = json.load(f)

#: spring problem boxplots

fit_keys = [alg_desc[x] for x in fit_results]

fit_values = fit_results.values()

plt.close('all')

plt.boxplot(fit_values, labels=fit_keys)

plt.title("Pressure Vessel Design (Original) - Boxplot")

plt.savefig("latex/images/pressure_vessel_problem_original_boxplot.png", dpi=600)

content = """\\begin{figure}[H]
\\centering
\\caption{Boxplot for Pressure Vessel Design (Original)}
\\label{fig:pressure_vessel_design_original_boxplot}
\\includegraphics[scale=0.5]{images/pressure_vessel_problem_original_boxplot.png}
\\end{figure}
"""
with open("latex/includes/pressure_vessel_problem_original_boxplot.tex", "w") as f:
    f.write(content)

