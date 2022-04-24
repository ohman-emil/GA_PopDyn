# https://www.youtube.com/watch?v=Gg--FOdupwY

from numpy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# dA/dt = -k A B    A(0) = 2
# dB/dt = -k A B    B(0) = 1
# dC/dt = k A B    C(0) = 0
# k = 0.1

# define model
def func(t,y):
    k = 0.1

    dA_dt = -k*y[0]*y[1]
    dB_dt = -k*y[0]*y[1]
    dC_dt = k*y[0]*y[1]

    return [dA_dt, dB_dt, dC_dt]

t_span = [0, 50]
t = linspace(t_span[0], t_span[1])

initial = [2, 1, 0]

sol = solve_ivp(func, t_span, initial, method='LSODA', t_eval=t) # solve ODE
plt.plot(sol.t, sol.y[0], label="y[0]") # plot it
plt.plot(sol.t, sol.y[1], label="y[1]") # plot it
plt.plot(sol.t, sol.y[2], label="y[2]") # plot it

# plot results
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()