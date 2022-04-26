from numpy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import json
import sys
import os

sys.path.append(os.path.join(sys.path[0], '..', 'helpers'))
import roman

# matplotlib settings
plt.style.use('seaborn-whitegrid')

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
plt.legend()
plt.show()