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
    content += f.read()

#: spring problem
content += "\\subsection{Spring Tension Design}\n\n"
content += "\\label{ssubec:spring_problem}"


content += "\\subsubsection{Evolutionary Algorithms}\n\n"
content += "\\label{subsubsec:spring_problem_evolutionary_based}\n\n"

content += "\\subsubsection{Swarm Based Algorithms}\n\n"
content += "\\label{subsubsec:spring_problem_swarm_based}\n\n"

# pressure vessel problem

content += "\\subsection{Pressure Vessel Design}\n\n"
content += "\\label{subsec:pressure_vessel_problem}"

content += "\\subsubsection{Evolutionary Algorithms}\n\n"
content += "\\label{subsubsec:pressure_vessel_problem_evolutionary_based}\n\n"

content += "\\subsubsection{Swarm Based Algorithms}\n\n"
content += "\\label{subsubsec:pressure_vessel_problem_swarm_based}\n\n"

# Friedman's test

# footer

with open("latex/includes/footer.tex", "r") as f:
    content += f.read()

with open("latex/article.tex", "w") as f:
    f.write(content)
