# statistical tests - https://github.com/citiususc/stac
from Functions import *
from Solvers import *
from mealpy.swarm_based import PSO
import numpy as np

s_lb = spring_get_lb()

s_ub = spring_get_ub()

p_lb = pressure_vessel_get_lb()

p_ub = pressure_vessel_get_ub()

spring = Spring(lb=s_lb, ub=s_ub, minmax='min')

pressure_vessel = PressureVessel(lb=p_lb, ub=p_ub, minmax='min')

epochs = 50

pop_size = 50

runs = 50

results = dict()

for seed in range(1, runs+1):

    best_position, best_fitness = solve_ep(seed, spring, epochs, pop_size)
    if "SpringEP" not in results:
        results["SpringEP"] = list()
    results["SpringEP"].append([best_position, best_fitness])

    best_position, best_fitness = solve_es(seed, spring, epochs, pop_size)
    if "SpringES" not in results:
        results["SpringES"] = list()
    results["SpringES"].append([best_position, best_fitness])

    best_position, best_fitness = solve_ga(seed, spring, epochs, pop_size)
    if "SpringGA" not in results:
        results["SpringGA"] = list()
    results["SpringGA"].append([best_position, best_fitness])

    best_position, best_fitness = solve_beesa(seed, spring, epochs, pop_size)
    if "SpringBEESA" not in results:
        results["SpringBEESA"] = list()
    results["SpringBEESA"].append([best_position, best_fitness])

    best_position, best_fitness = solve_ffa(seed, spring, epochs, pop_size)
    if "SpringFFA" not in results:
        results["SpringFFA"] = list()
    results["SpringFFA"].append([best_position, best_fitness])

    best_position, best_fitness = solve_pso(seed, spring, epochs, pop_size)
    if "SpringPSO" not in results:
        results["SpringPSO"] = list()
    results["SpringPSO"].append([best_position, best_fitness])

    best_position, best_fitness = solve_ep(seed, pressure_vessel, epochs, pop_size)
    if "PressureEP" not in results:
        results["PressureEP"] = list()
    results["PressureEP"].append([best_position, best_fitness])

    best_position, best_fitness = solve_es(seed, pressure_vessel, epochs, pop_size)
    if "PressureES" not in results:
        results["PressureES"] = list()
    results["PressureES"].append([best_position, best_fitness])

    best_position, best_fitness = solve_ga(seed, pressure_vessel, epochs, pop_size)
    if "PressureGA" not in results:
        results["PressureGA"] = list()
    results["PressureGA"].append([best_position, best_fitness])

    best_position, best_fitness = solve_beesa(seed, pressure_vessel, epochs, pop_size)
    if "PressureBEESA" not in results:
        results["PressureBEESA"] = list()
    results["PressureBEESA"].append([best_position, best_fitness])

    best_position, best_fitness = solve_ffa(seed, pressure_vessel, epochs, pop_size)
    if "PressureFFA" not in results:
        results["PressureFFA"] = list()
    results["PressureFFA"].append([best_position, best_fitness])

    best_position, best_fitness = solve_pso(seed, pressure_vessel, epochs, pop_size)
    if "PressurePSO" not in results:
        results["PressurePSO"] = list()
    results["PressurePSO"].append([best_position, best_fitness])

print(results)