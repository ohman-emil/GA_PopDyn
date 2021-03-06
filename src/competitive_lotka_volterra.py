import time
time_start = time.perf_counter() # start timer

from numpy import linspace
from scipy.integrate import solve_ivp
import tikzplotlib
import matplotlib.pyplot as plt
import json
import sys
import os

sys.path.append(os.path.join(sys.path[0], '..', 'helpers'))
import roman

time_modules = time.perf_counter() # time to import modules

# matplotlib settings
plt.style.use('seaborn-whitegrid')
plt.rcParams["figure.figsize"] = (16,8)

# is there (still) a better data structre?
data = json.load(open(f'./src/data/competitive_lotka_volterra/{sys.argv[1]}.json'))

# define model
def func(t, y, data):
    res = [] # one item for every species

    for i in range(data['n']):
        interactions = 0 # for the sum over k in the formula
        for j, value in enumerate(data["interaction_matrix"][i]):
            interactions += value * y[j]

        res.append(data['r'][i] * y[i] * (1 - (interactions / data['k'][i]))) # formula (see https://en.wikipedia.org/wiki/Competitive_Lotka%E2%80%93Volterra_equations#N_species)

    return res

# time stuff
t_span = data["t_span"]
t = linspace(t_span[0], t_span[1], 2*t_span[1])

# get inital values
initial = []
for i in data["t0"]:
    initial.append(i)

sol = solve_ivp(func, t_span, initial, method='LSODA', t_eval=t, args=(data,)) # solve ODE

# loop through every species and plot it
for i, item in enumerate(sol.y):
    plt.plot(sol.t, item, label=roman.int_to_roman(i))

plt.plot(sol.t, sum(sol.y), alpha=0.75, linestyle='--', label="SUM") # create a line with total biomass

# plot results
plt.xlabel('time')
plt.ylabel('biomass')
plt.legend(loc="lower center", bbox_to_anchor=(0.5, 1), ncol=5, fontsize="xx-large")

# display time
time_end = time.perf_counter()
print(f"\
    Total time: {round(time_end-time_start, 5)} s\n\
    Module time: {round(time_modules-time_start, 5)} s\n\
    Execution time: {round(time_end-time_modules, 5)} s"
)

# tikzplotlib.save('test.tex')

# show diagram
plt.show()
