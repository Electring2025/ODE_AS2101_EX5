import math
from cmath import sqrt

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.integrate as solve_ivp

g=9.81
A_tank=8
A_outlet=0.04
initial_fuel_height=4.5

time = (0, 150)

def f(t, y):
    dydt = -A_outlet*np.sqrt(np.abs(y[0]))*np.sqrt(2*g)/A_tank
    return dydt

solution = scipy.integrate.solve_ivp(f, time, [initial_fuel_height], t_eval=np.linspace(0, 150, 100))

def plot(t, y):
    plt.plot(solution.t,solution.y[0])
    plt.xlabel('Time')
    plt.ylabel('y(t)')
    plt.title('Solution of ODE')
    plt.grid()
    plt.show()
    plt.savefig('ODE')

plot(time,solution)
