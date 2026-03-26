import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.integrate as solve_ivp

time = (0, 10)

def f(t, y):
    dydt = np.sin(t)
    return dydt

solution = scipy.integrate.solve_ivp(f, time, [-1], t_eval=np.linspace(0, 10, 100))

def plot(t, y):
    plt.plot(solution.t,solution.y[0])
    plt.xlabel('Time')
    plt.ylabel('y(t)')
    plt.title('Solution of ODE')
    plt.grid()
    plt.show()
    plt.savefig('ODE')

plot(time,solution)
