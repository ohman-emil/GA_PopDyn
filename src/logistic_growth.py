from numpy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# matplotlib settings
plt.style.use('seaborn-whitegrid')

# N = biomass
# t = time
# r = growth rate
# K = carrying capacity

# define model
def func(t,N,r,K):
    dydt = r*N*(1-(N/K))
    return dydt

def plotODE(model, y0, t_span, r, K):
    t = linspace(t_span[0], t_span[1])
    sol = solve_ivp(model, t_span, y0, args=(r,K), method='LSODA', t_eval=t) # solve ODE
    plt.plot(sol.t, sol.y[0]) # plot it

plotODE(func, [10], [0, 100], 0.05, 500) # model, [y0], [t0, t_end], growth_rate, carrying_capacity
plotODE(func, [10], [0, 100], 0.1, 500)

# plot results
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()