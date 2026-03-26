import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(state, t, b, g, l, m):
    # Unpack state: state[0] = theta (position), state[1] = omega (velocity)
    theta, omega = state

    # Define the system of first-order ODEs
    # dtheta/dt = omega
    # domega/dt = -(b/m)*omega - (g/l)*sin(theta)
    dtheta_dt = omega
    domega_dt = -(b / m) * omega - (g / l) * np.sin(theta)

    return [dtheta_dt, domega_dt]


# Parameters
b = 0.05  # damping coefficient
g = 9.81  # gravity
l = 1.0  # length
m = 0.1  # mass

# Initial conditions: [theta_0, omega_0]
theta_0 = [0, 3]

# Time points
t = np.linspace(0, 20, 150)

# Solve the ODE
# The .T transposes the result to separate position and velocity columns
theta, omega = odeint(model, theta_0, t, args=(b, g, l, m)).T

# Plotting
plt.plot(t, theta, label='Displacement')
plt.plot(t, omega, label='Velocity')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()