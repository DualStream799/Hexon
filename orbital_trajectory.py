import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import math
import json
# Unidades Astronômicas para conversão
UA = 149597870700 # m
P = 3.156*10**7   # s
# Distâncias Periélio
dist_sun_merc = 46001200000/UA # UA
dist_sun_ven = 107476000000/UA  # UA
dist_sun_ear = 147098290000/UA  # UA
dist_sun_mars = 227900000000/UA # UA 
dist_sun_jup = 778500000000/UA  # UA
dist_sun_sat = 1353572956000/UA # UA
dist_sun_ur = 2748938461000/UA  # UA
dist_sun_net = 4452940833000/UA # UA
# Velocidades Orbitais
Vorb_merc = 47.362*10**3/UA*P  # ano/UA
Vorb_ven = 35.02*10**3/UA*P    # ano/UA
Vorb_ear = 29.78*10**3/UA*P    # ano/UA
Vorb_mars = 24.077*10**3/UA*P  # ano/UA
Vorb_jup = 13.07*10**3/UA*P    # ano/UA
Vorb_sat = 9.69*10**3/UA*P     # ano/UA
Vorb_ur = 6.81*10**3/UA*P      # ano/UA
Vorb_net = 5.43*10**3/UA*P     # ano/UA
# Condições iniciais [x0, y0, Vx0, Vy0]
val_merc = [dist_sun_merc, 0, 0, Vorb_merc]
val_ven = [dist_sun_ven, 0, 0, Vorb_ven]
val_ear = [dist_sun_ear, 0, 0, Vorb_ear]
val_mars = [dist_sun_mars, 0, 0, Vorb_mars]
val_jup = [dist_sun_jup, 0, 0, Vorb_jup]
val_sat = [dist_sun_sat, 0, 0, Vorb_sat]
val_ur = [dist_sun_ur, 0, 0, Vorb_ur]
val_net = [dist_sun_net, 0, 0, Vorb_net]
# Equações difereniais
def EqDif(val_init, t):
    # Valores iniciais:
    x = val_init[0]
    y = val_init[1]
    Vx = val_init[2]
    Vy = val_init[3]
    # Derivadas:
    dxdt = Vx
    dydt = Vy
    dVxdt = -4*math.pi**2*(x/(x**2 + y**2)**(3/2))
    dVydt = -4*math.pi**2*(y/(x**2 + y**2)**(3/2))
    return [dxdt, dydt, dVxdt, dVydt]
# Lista tempo
time = np.arange(0, 58, 1)
# Integração Numérica
solution_mercury = odeint(EqDif, val_merc, time)
solution_venus = odeint(EqDif, val_ven, time)
solution_earth = odeint(EqDif, val_ear, time)
solution_mars = odeint(EqDif, val_mars, time)
solution_jupiter = odeint(EqDif, val_jup, time)
solution_saturn = odeint(EqDif, val_sat, time)
solution_uranus = odeint(EqDif, val_ur, time)
solution_net = odeint(EqDif, val_net, time)

plt.scatter(117*solution_earth[:, 0], 117*solution_earth[:, 1])
plt.grid()
plt.show()

print((list(117*solution_earth[:,0])))
print((list(117*solution_earth[:,1])))
