from numpy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# is there (still) a better data structre?
data = {
    "n": 3, # no. of species
    "r": [0.05, 0.1, 0.2],
    "k": [100, 75, 150],
    "t0": [30, 10, 5],
    "interaction_matrix": [[1, 2, 2.5], [0.75, 1, 0.75], [0, 5, 1]]
}

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
t_span = [0, 150]
t = linspace(t_span[0], t_span[1], 2*t_span[1])

# get inital values
initial = []
for i in range(data['n']):
    initial.append(data["t0"][i])

sol = solve_ivp(func, t_span, initial, method='LSODA', t_eval=t, args=(data,)) # solve ODE

# loop through every species and plot it
for i, item in enumerate(sol.y):
    plt.plot(sol.t, item, label=f"y{i}")

# plot results
plt.xlabel('time')
plt.ylabel('biomass')
plt.legend()
plt.show()