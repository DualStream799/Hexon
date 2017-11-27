import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
from math import pi
import json

radius = 117
def orbital_trajectory(radius):
    """
    Creates couple of lists (X-axis and Y-axis position lists) 
    based on Earth translation around the Sun.

    Libraries importation required:
    - odeint ( from sicipy.integrate import odeint )
    - np     ( import numpy as np )
    - pi     ( from math import pi )

    Parameters:
    - radius (int or float value)

    Returns: 
    - solution_pixels_rounded (numpy.ndarray)
    """

    # Unit converters:
    AU = 149597870700  # Astronomic Unit in m
    P = 3.156*10**7    # year in seconds
    # Initials Conditions [x0, y0, Vx0, Vy0]:
    val_init = [1, 0, 0, 29.78*10**3/AU*P]
    # Differential Equations:
    def EqDif(val_init, t):
        # Loading initial values:
        x = val_init[0]
        y = val_init[1]
        Vx = val_init[2]
        Vy = val_init[3]
        # Derivatives:
        dxdt = Vx
        dydt = Vy
        dVxdt = -4*pi**2*(x/(x**2 + y**2)**(3/2))
        dVydt = -4*pi**2*(y/(x**2 + y**2)**(3/2))
        return [dxdt, dydt, dVxdt, dVydt]
    # Time list:
    time = np.arange(0, 1, 1/360)
    # Numeric integration:
    solution = odeint(EqDif, val_init, time)
    # Converting values (in AU) for screen size proportion (pixels):
    solution_pixels = radius*solution
    # Rounding numpers for int numbers (pixels are always int values):
    solution_pixels_rounded = np.around(solution_pixels)
    # Returned data
    return solution_pixels_rounded

print(orbital_trajectory(radius))
orbital_trajectory(radius)

plt.plot(orbital_trajectory(radius)[:, 1])
plt.grid()
plt.show()
plt.figure(figsize=(5, 5))
plt.plot(orbital_trajectory(radius)[:,2], orbital_trajectory(radius)[:, 0])
plt.grid()
plt.show()

help(round)
