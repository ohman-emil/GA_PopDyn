from numpy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Is there a better data structre?
effects = [[1, 2], [0.75, 1]]
constants = [
    {"r": 0.05, "k": 100, "t0": 30},
    {"r": 0.1, "k": 75, "t0": 10}
]

# define model
def func(t, y, e, c):
    dy0_dt = c[0]['r'] * y[0] * (1 - ((y[0] + e[0][1]*y[1]) / c[0]['k']))
    dy1_dt = c[1]['r'] * y[1] * (1 - ((y[1] + e[1][0]*y[0]) / c[1]['k']))
    return [dy0_dt, dy1_dt]

t_span = [0, 150]
t = linspace(t_span[0], t_span[1], 2*t_span[1])

initial = [constants[0]['t0'], constants[1]['t0']] # initial values

sol = solve_ivp(func, t_span, initial, method='LSODA', t_eval=t, args=(effects, constants,)) # solve ODE
plt.plot(sol.t, sol.y[0], label="y0") # plot
plt.plot(sol.t, sol.y[1], label="y1") # plot

# plot results
plt.xlabel('time')
plt.ylabel('biomass')
plt.legend()
plt.show()