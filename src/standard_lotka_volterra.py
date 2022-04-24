# https://www.cs.unm.edu/~forrest/classes/cs365/lectures/Lotka-Volterra.pdf

from numpy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# x = number of prey
# y = number of predator

# a = natural growth of x (prey)
# b = rate of predation
# c = natural growth of y (predator)
# d = natural death of y (predator)

# dx/dt = ax - bxy
# dy/dt = cxy - dy

a = 0.1
b = 0.02
c = 0.02
d = 0.4

# define model
def func(t, y, a, b, c, d):
    dx_dt = (a*y[0]) - (b*y[0]*y[1])
    dy_dt = (c*y[0]*y[1]) - (d*y[1])

    return [dx_dt, dy_dt]

t_span = [0, 150]
t = linspace(t_span[0], t_span[1], 2*t_span[1])

initial = [15, 10] # initial values

sol = solve_ivp(func, t_span, initial, method='LSODA', t_eval=t, args=(a, b, c, d,)) # solve ODE
plt.plot(sol.t, sol.y[0], label="y[0]") # plot
plt.plot(sol.t, sol.y[1], label="y[1]") # plot

# plot results
plt.xlabel('time')
plt.ylabel('biomass')
plt.legend()
plt.show()