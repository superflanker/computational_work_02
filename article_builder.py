"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Article Builder
"""

content = ""

#: header
with open("latex/includes/header.tex", "r") as f:
    content += f.read() + "\n"

# pressure vessel problem

content += "\\subsection{Pressure Vessel Design (Original)}\n"
content += "\\label{subsec:pressure_vessel_problem_original}\n\n"

with open("latex/includes/pressure_vessel_problem_original_best_fits.tex", "r") as f:
    content += f.read() + "\n"

with open("latex/includes/pressure_vessel_problem_original.tex", "r") as f:
    content += f.read() + "\n"

with open("latex/includes/pressure_vessel_problem_original_boxplot.tex", "r") as f:
    content += f.read() + "\n"

with open("latex/includes/pressure_vessel_problem_original_convergence.tex", "r") as f:
    content += f.read() + "\n"

# pressure vessel problem

content += "\\subsection{Pressure Vessel Design}\n"
content += "\\label{subsec:pressure_vessel_problem}\n\n"

with open("latex/includes/pressure_vessel_problem_best_fits.tex", "r") as f:
    content += f.read() + "\n"

with open("latex/includes/pressure_vessel_problem.tex", "r") as f:
    content += f.read() + "\n"

with open("latex/includes/pressure_vessel_problem_boxplot.tex", "r") as f:
    content += f.read() + "\n"

with open("latex/includes/pressure_vessel_problem_convergence.tex", "r") as f:
    content += f.read() + "\n"

#: spring problem
content += "\\subsection{Spring Tension Design}\n"
content += "\\label{ssubec:spring_problem}\n\n"

with open("latex/includes/spring_problem_best_fits.tex", "r") as f:
    content += f.read() + "\n"

with open("latex/includes/spring_problem.tex", "r") as f:
    content += f.read() + "\n"

with open("latex/includes/spring_problem_boxplot.tex", "r") as f:
    content += f.read() + "\n"

with open("latex/includes/spring_problem_convergence.tex", "r") as f:
    content += f.read() + "\n"

# Friedman's test

content += "\\subsection{Significance Test}\n"
content += "\\label{subsec:pressure_vessel_problem_significance_test}\n\n"

with open("latex/includes/friedman_test.tex", "r") as f:
    content += f.read() + "\n"

# footer

with open("latex/includes/footer.tex", "r") as f:
    content += f.read() + "\n"

with open("latex/article.tex", "w") as f:
    f.write(content)
