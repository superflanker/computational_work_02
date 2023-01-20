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


def latex_best_fits_table(results,
                          desc,
                          problem):

    column_names = ["Algorithm"]

    var_num = len(results[0]) - 2

    for i in range(1, var_num + 1):
        var_col_name = "x_{:d}".format(i)
        column_names.append('$' + var_col_name + '$')

    column_names.append('$f_x$')

    df = pd.DataFrame(results,
                      columns=column_names)

    content = df.to_latex(index=False,
                          float_format="%.8f",
                          escape=False,
                          label="best_fits:{:s}".format(problem),
                          caption="Best Fits for {:s}".format(desc))

    return content


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

with open("results/joined_best_fits.json", "r") as f:
    best_fits = json.load(f)

for problem in data:

    desc = data[problem]['desc']

    results = data[problem]['results']

    content = latex_results_table(results,
                                  desc,
                                  problem)

    with open("latex/includes/{:s}.tex".format(problem), "w") as f:
        f.write(content)

    results = best_fits[problem]

    content = latex_best_fits_table(results,
                                    desc,
                                    problem)

    with open("latex/includes/{:s}_best_fits.tex".format(problem), "w") as f:
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
    plt.close('all')
    fig, axs = plt.subplots(3, 2, figsize=(10, 10))

    #: EP

    s_min = population_data[problem]['solve_ep']['min']
    s_max = population_data[problem]['solve_ep']['max']
    s_mean = population_data[problem]['solve_ep']['avg']

    x = np.linspace(1, len(s_min), len(s_min))

    axs[0][0].plot(x, s_min, label="Min Values")
    axs[0][0].plot(x, s_mean, label="Mean Values")
    axs[0][0].plot(x, s_max, label="Max Values")
    axs[0][0].set_xlabel('Epochs')
    axs[0][0].set_ylabel('Obj. Fun Values(log)')
    axs[0][0].set_yscale('log')
    axs[0][0].set_title(alg_desc['solve_ep'])
    axs[0][0].legend()
    axs[0][0].grid(True)

    #: ES

    s_min = population_data[problem]['solve_es']['min']
    s_max = population_data[problem]['solve_es']['max']
    s_mean = population_data[problem]['solve_es']['avg']

    x = np.linspace(1, len(s_min), len(s_min))

    axs[0][1].plot(x, s_min, label="Min Values")
    axs[0][1].plot(x, s_mean, label="Mean Values")
    axs[0][1].plot(x, s_max, label="Max Values")
    axs[0][1].set_xlabel('Epochs')
    axs[0][1].set_ylabel('Obj. Fun Values(log)')
    axs[0][1].set_yscale('log')
    axs[0][1].set_title(alg_desc['solve_es'])
    axs[0][1].legend()
    axs[0][1].grid(True)

    #: GA

    s_min = population_data[problem]['solve_ga']['min']
    s_max = population_data[problem]['solve_ga']['max']
    s_mean = population_data[problem]['solve_ga']['avg']

    x = np.linspace(1, len(s_min), len(s_min))

    axs[1][0].plot(x, s_min, label="Min Values")
    axs[1][0].plot(x, s_mean, label="Mean Values")
    axs[1][0].plot(x, s_max, label="Max Values")
    axs[1][0].set_xlabel('Epochs')
    axs[1][0].set_ylabel('Obj. Fun Values(log)')
    axs[1][0].set_yscale('log')
    axs[1][0].set_title(alg_desc['solve_ga'])
    axs[1][0].legend()
    axs[1][0].grid(True)

    #: BeesA

    s_min = population_data[problem]['solve_beesa']['min']
    s_max = population_data[problem]['solve_beesa']['max']
    s_mean = population_data[problem]['solve_beesa']['avg']

    x = np.linspace(1, len(s_min), len(s_min))

    axs[1][1].plot(x, s_min, label="Min Values")
    axs[1][1].plot(x, s_mean, label="Mean Values")
    axs[1][1].plot(x, s_max, label="Max Values")
    axs[1][1].set_xlabel('Epochs')
    axs[1][1].set_ylabel('Obj. Fun Values(log)')
    axs[1][1].set_yscale('log')
    axs[1][1].set_title(alg_desc['solve_beesa'])
    axs[1][1].legend()
    axs[1][1].grid(True)

    #: FFA

    s_min = population_data[problem]['solve_ffa']['min']
    s_max = population_data[problem]['solve_ffa']['max']
    s_mean = population_data[problem]['solve_ffa']['avg']

    x = np.linspace(1, len(s_min), len(s_min))

    axs[2][0].plot(x, s_min, label="Min Values")
    axs[2][0].plot(x, s_mean, label="Mean Values")
    axs[2][0].plot(x, s_max, label="Max Values")
    axs[2][0].set_xlabel('Epochs')
    axs[2][0].set_ylabel('Obj. Fun Values(log)')
    axs[2][0].set_yscale('log')
    axs[2][0].set_title(alg_desc['solve_ffa'])
    axs[2][0].legend()
    axs[2][0].grid(True)

    #: PSO

    s_min = population_data[problem]['solve_pso']['min']
    s_max = population_data[problem]['solve_pso']['max']
    s_mean = population_data[problem]['solve_pso']['avg']

    x = np.linspace(1, len(s_min), len(s_min))

    axs[2][1].plot(x, s_min, label="Min Values")
    axs[2][1].plot(x, s_mean, label="Mean Values")
    axs[2][1].plot(x, s_max, label="Max Values")
    axs[2][1].set_xlabel('Epochs')
    axs[2][1].set_ylabel('Obj. Fun Values(log)')
    axs[2][1].set_yscale('log')
    axs[2][1].set_title(alg_desc['solve_pso'])
    axs[2][1].legend()
    axs[2][1].grid(True)


    fig.tight_layout()
    
    plt.savefig("latex/images/" + problem + "_convergence.png", dpi=600)

    content = """\\begin{figure}[H]
    \\centering
    \\caption{Convergence lines for """ + problem_desc[problem] + """}
    \\label{fig:""" + problem + "_convergence" + """}
    \\includegraphics[width=0.4 \\textwidth]{images/""" + problem + "_convergence"  +  """.png}
    \\end{figure}
    """
    with open("latex/includes/" + problem + "_convergence.tex", "w") as f:
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

