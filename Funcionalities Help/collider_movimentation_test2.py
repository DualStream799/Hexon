# Importing libraries:

import matplotlib.pyplot as plt
import numpy as np
from math import degrees
from math import atan
from math import sin
from math import cos

#          
val_init = [-255, 300, 0, 0]
def collider_moviementation(init_values, step):
	'''Recieve two points in Carteisan system (2 doubles of tuples)
	and calclates the linear function which connect them.

	Libraries importation required:
		    - randint ( from numpy import linspace )

	Parameters:
		- init_values (list) : [ x1, y1, x2, y2]
		- step (integer or float)

	Returns:
		- [xlist, ylist] (list of lists)
	'''
	# Loading values
	x1 = init_values[0]
	y1 = init_values[1]
	x2 = init_values[2]
	y2 = init_values[3]
	# Angular Coeficient:
	m = (y1 - y2)/(x1 - x2)
	# Linear Coeficient:
	b = y1 - m*x1
	# X and Y values list:
	xlist = np.linspace(x1, x2, step)
	ylist = []

	for x_val in xlist:
		y_val = m*x_val + b
		ylist.append(y_val)

	return [xlist, ylist]

solution0 = collider_moviementation([-225, 0, 0, 0], 10)
solution1 = collider_moviementation([-225, 100, 0, 0], 10)
solution2 = collider_moviementation([-225, 200, 0, 0], 10)
solution3 = collider_moviementation([-225, 300, 0, 0], 10)
solution4 = collider_moviementation([-225, 400, 0, 0], 10)
solution5 = collider_moviementation([-225, 500, 0, 0], 10)
solution6 = collider_moviementation([-225, 600, 0, 0], 10)
solution7 = collider_moviementation([-225, 700, 0, 0], 10)
solution8 = collider_moviementation([-225, 800, 0, 0], 10)

solution9 = collider_moviementation([225, 0, 0, 0], 10)
solution10 = collider_moviementation([225, 100, 0, 0], 10)
solution11 = collider_moviementation([225, 200, 0, 0], 10)
solution12 = collider_moviementation([225, 300, 0, 0], 10)
solution13 = collider_moviementation([225, 400, 0, 0], 10)
solution14 = collider_moviementation([225, 500, 0, 0], 10)
solution15 = collider_moviementation([225, 600, 0, 0], 10)
solution16 = collider_moviementation([225, 700, 0, 0], 10)
solution17 = collider_moviementation([225, 800, 0, 0], 10)

solution18 = collider_moviementation([-225, 0, 0, 0], 10)
solution19 = collider_moviementation([-225, -100, 0, 0], 10)
solution20 = collider_moviementation([-225, -200, 0, 0], 10)
solution21 = collider_moviementation([-225, -300, 0, 0], 10)
solution22 = collider_moviementation([-225, -400, 0, 0], 10)
solution23 = collider_moviementation([-225, -500, 0, 0], 10)
solution24 = collider_moviementation([-225, -600, 0, 0], 10)
solution25 = collider_moviementation([-225, -700, 0, 0], 10)
solution26 = collider_moviementation([-225, -800, 0, 0], 10)

solution27 = collider_moviementation([225, 0, 0, 0], 10)
solution28 = collider_moviementation([225, -100, 0, 0], 10)
solution29 = collider_moviementation([225, -200, 0, 0], 10)
solution30 = collider_moviementation([225, -300, 0, 0], 10)
solution31 = collider_moviementation([225, -400, 0, 0], 10)
solution32 = collider_moviementation([225, -500, 0, 0], 10)
solution33 = collider_moviementation([225, -600, 0, 0], 10)
solution34 = collider_moviementation([225, -700, 0, 0], 10)
solution35 = collider_moviementation([225, -800, 0, 0], 10)


plt.scatter(solution0[0][:], solution0[1][:])
plt.scatter(solution1[0][:], solution1[1][:])
plt.scatter(solution2[0][:], solution2[1][:])
plt.scatter(solution3[0][:], solution3[1][:])
plt.scatter(solution4[0][:], solution4[1][:])
plt.scatter(solution5[0][:], solution5[1][:])
plt.scatter(solution6[0][:], solution6[1][:])
plt.scatter(solution7[0][:], solution7[1][:])
plt.scatter(solution8[0][:], solution8[1][:])
plt.scatter(solution9[0][:], solution9[1][:])
plt.scatter(solution10[0][:], solution10[1][:])
plt.scatter(solution11[0][:], solution11[1][:])
plt.scatter(solution12[0][:], solution12[1][:])
plt.scatter(solution13[0][:], solution13[1][:])
plt.scatter(solution14[0][:], solution14[1][:])
plt.scatter(solution15[0][:], solution15[1][:])
plt.scatter(solution16[0][:], solution16[1][:])
plt.scatter(solution17[0][:], solution17[1][:])
plt.scatter(solution18[0][:], solution18[1][:])
plt.scatter(solution19[0][:], solution19[1][:])
plt.scatter(solution20[0][:], solution20[1][:])
plt.scatter(solution21[0][:], solution21[1][:])
plt.scatter(solution22[0][:], solution22[1][:])
plt.scatter(solution23[0][:], solution23[1][:])
plt.scatter(solution24[0][:], solution24[1][:])
plt.scatter(solution25[0][:], solution25[1][:])
plt.scatter(solution26[0][:], solution26[1][:])
plt.scatter(solution27[0][:], solution27[1][:])
plt.scatter(solution28[0][:], solution28[1][:])
plt.scatter(solution29[0][:], solution28[1][:])
plt.scatter(solution30[0][:], solution30[1][:])
plt.scatter(solution31[0][:], solution31[1][:])
plt.scatter(solution32[0][:], solution32[1][:])
plt.scatter(solution33[0][:], solution33[1][:])
plt.scatter(solution34[0][:], solution34[1][:])
plt.scatter(solution35[0][:], solution35[1][:])

plt.grid()
plt.show()

