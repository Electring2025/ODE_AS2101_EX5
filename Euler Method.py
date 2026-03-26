import numpy as np
import matplotlib . pyplot as plt


g = 9.81
A_tank = 8
A_outlet = 0.04
initial_fuel_height = 4.5
tf = 150
time_step = 0.1

iterations = int(np.floor(tf/time_step))

def euler_method (f, y0 , t):

    n = len (t)
    y = np. zeros (n)
    y[0] = y0

    for i in range (n -1):
        if y[i]>0:
            h = t[i + 1] - t[i]
            y[i + 1] = y[i] + h * f(t[i], y[i])
        else:
            y[i+1]=0

    return y


def my_ode (t, y):
    return -A_outlet * np.sqrt (np.abs (y)) * np.sqrt (2 * g) / A_tank

t = np. linspace (0, tf, iterations)
y = euler_method (my_ode , initial_fuel_height , t)

plt . plot (t, y, 'o-',marker=',', mec='red' ,mfc ='red',label=str(time_step))
plt . xlabel ('time(s)')
plt . ylabel ('Height of fuel (m)')
plt . title ('Euler Method Solution: Time Step = '+str(time_step)+'s')
plt . grid ( True )
plt . show ()