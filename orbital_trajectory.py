import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import math
import json
# Astronomical Units for convertion:
UA = 149597870700               # m
P = 3.156*10**7                 # s
# Perihelion Distance:
dist_sun_ear = 147098290000/UA  # UA
# Orbital Speed:
Vorb_ear = 29.78*10**3/UA*P     # ano/UA
# Initials Conditions [x0, y0, Vx0, Vy0]:
val_ear = [dist_sun_ear, 0, 0, Vorb_ear]
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
    dVxdt = -4*math.pi**2*(x/(x**2 + y**2)**(3/2))
    dVydt = -4*math.pi**2*(y/(x**2 + y**2)**(3/2))
    return [dxdt, dydt, dVxdt, dVydt]
# Tiem list:
time = np.arange(0, 58, 0.1)
# Numeric integration:
solution_earth = odeint(EqDif, val_ear, time)
# Graphic exibition of the trajectory:
plt.figure(figsize = (5, 5))
plt.plot(solution_earth[:, 0], solution_earth[:, 1])
plt.grid()
plt.show()
# Converting values for screen size (pixels):
listX = list(117*solution_earth[:,0])
listY = list(117*solution_earth[:,1])
NewListX = []
NewListY = []
for valx in listX:
    round_valx = round(valx)
    NewListX.append(round_valx)
for valy in listY:
    round_valy = round(valy)
    NewListY.append(round_valy)
    
print(NewListX)
print(NewListY)