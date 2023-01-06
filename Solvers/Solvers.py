
"""
Computational Work 02 - Evolutionary Computation
Authors: Augusto Mathias Adams - augusto.adams@ufpr.br - GRR20172143
         Caio Phillipe Mizerkowski - caiomizerkowski@gmail.com - GRR20166403
         Christian Piltz Araújo - christian0294@yahoo.com.br - GRR20172197
         Vinícius Eduardo dos Reis - eduardo.reis02@gmail.com - GRR20175957

Evolutionary Algorithms Solvers based on mealpy package
"""

from mealpy.evolutionary_based import ES, EP, GA
from mealpy.swarm_based import BeesA, FFA, PSO
import numpy as np

def solve_ep(seed,
             problem,
             epochs,
             pop_size,
             bout_size=0.1):

    """
    Evolutionary Programming
    :param seed: random seed
    :param problem: problem class
    :param epochs: epochs
    :param pop_size: population size
    :param bout_size: percentage of child agents implement tournament selection
    :return: best_solution, best_fitness
    """

    np.random.seed(seed)

    model = EP.LevyEP(epoch=epochs,
                      pop_size=pop_size,
                      bout_size=bout_size)

    best_position, best_fitness = model.solve(problem=problem)
    return best_position, best_fitness

def solve_es(seed,
             problem,
             epochs,
             pop_size,
             lamda=0.5):

    """
    Evolutionary Strategy
    :param seed: random seed
    :param problem: problem class
    :param epochs: epochs
    :param pop_size: population size
    :param lamda: Percentage of child agents evolving in the next generation
    :return: best_position, best_fitness
    """

    np.random.seed(seed)

    model = ES.OriginalES(epoch=epochs,
                          pop_size=pop_size,
                          lamda=lamda)

    best_position, best_fitness = model.solve(problem=problem)
    return best_position, best_fitness

def solve_ga(seed,
             problem,
             epochs,
             pop_size,
             pc=0.95,
             pm=0.025):

    """
    Genetic Algorithm
    :param seed: random seed
    :param problem: problem class
    :param epochs: epochs
    :param pop_size: population size
    :param pc: cross-over probability
    :param pm: mutation probability
    :return: best_position, best_fitness
    """

    np.random.seed(seed)

    model = GA.BaseGA(epoch=epochs,
                      pop_size=pop_size,
                      pc=pc,
                      pm=pm)

    best_position, best_fitness = model.solve(problem=problem)
    return best_position, best_fitness


def solve_beesa(seed,
                problem,
                epochs,
                pop_size,
                selected_site_ratio=0.5,
                elite_site_ratio=0.4,
                selected_site_bee_ratio=0.1,
                elite_site_bee_ratio=2,
                dance_radius=0.1,
                dance_reduction=0.99):

    """
    Bees Algorithm
    :param seed: random seed
    :param problem: problem class
    :param epochs: epochs
    :param pop_size: population size
    :param selected_site_ratio: hyperparameter
    :param elite_site_ratio: hyperparameter
    :param selected_site_bee_ratio: hyperparameter
    :param elite_site_bee_ratio: hyperparameter
    :param dance_radius: hyperparameter
    :param dance_reduction: hyperparameter
    :return: best_position, best_fitness
    """

    np.random.seed(seed)

    model = BeesA.OriginalBeesA(epoch=epochs,
                                pop_size=pop_size,
                                selected_site_ratio=selected_site_ratio,
                                elite_site_ratio=elite_site_ratio,
                                selected_site_bee_ratio=selected_site_bee_ratio,
                                elite_site_bee_ratio=elite_site_bee_ratio,
                                dance_radius=dance_radius,
                                dance_reduction=dance_reduction)

    best_position, best_fitness = model.solve(problem=problem)
    return best_position, best_fitness

def solve_ffa(seed,
              problem,
              epochs,
              pop_size,
              gamma=0.001,
              beta_base=2,
              alpha=0.2,
              alpha_damp=0.99,
              delta=0.05,
              exponent=2):

    """
    Firefly Algorithm
    :param seed: random seed
    :param problem: problem class
    :param epochs: epochs
    :param pop_size: population size
    :param gamma: Light Absorption Coefficient
    :param beta_base: Attraction Coefficient Base Value
    :param alpha: Mutation Coefficient
    :param alpha_damp: Mutation Coefficient Damp Rate
    :param delta: Mutation Step Size
    :param exponent: Exponent
    :return: best_position, best_fitness
    """

    np.random.seed(seed)

    model = FFA.OriginalFFA(epoch=epochs,
                            pop_size=pop_size,
                            gamma=gamma,
                            beta_base=beta_base,
                            alpha=alpha,
                            alpha_damp=alpha_damp,
                            delta=delta,
                            exponent=exponent)

    best_position, best_fitness = model.solve(problem=problem)
    return best_position, best_fitness

def solve_pso(seed,
              problem,
              epochs,
              pop_size,
              c1=2.05,
              c2=2.05,
              w_min=0.4,
              w_max=0.9):

    """
    Particle Swarm Optimization
    :param seed: random seed
    :param problem: problem class
    :param epochs: epochs
    :param pop_size: population size
    :param c1: local coefficient
    :param c2: global coefficient
    :param w_min: weight min of bird
    :param w_max: weight max of bird
    :return: best_position, best_fitness
    """

    np.random.seed(seed)

    model = PSO.OriginalPSO(epoch=epochs,
                            pop_size=pop_size,
                            c1=c1,
                            c2=c2,
                            w_min=w_min,
                            w_max=w_max)

    best_position, best_fitness = model.solve(problem=problem)
    return best_position, best_fitness