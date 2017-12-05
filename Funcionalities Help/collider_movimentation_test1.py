# Importing libraries:

import matplotlib.pyplot as plt
import numpy as np
from math import degrees
from math import atan
from math import sin
from math import cos


def collider_angulation(pos_x, pos_y, speed, time):
	listx = []
	listy = []
	time_list = [0]
	listx.append(pos_x)
	listy.append(pos_y)
	angle = - degrees(atan((800/2 - pos_y)/(450/2 - pos_x))) + 180
	delta_x = cos(angle)*speed
	delta_y = sin(angle)*speed
	print(angle)
	for t in range(1, time-1):
		new_x = listx[-1]+delta_x
		new_y = listy[-1]-delta_y
		listx.append(new_x)
		listy.append(new_y)
		time_list.append(t)
	return [time_list, listx, listy]

solution0 = collider_angulation(0, 0, 10, 100)
solution1 = collider_angulation(0, 100, 10, 100)
solution2 = collider_angulation(0, 200, 10, 100)
solution3 = collider_angulation(0, 300, 10, 100)
solution4 = collider_angulation(0, 400, 10, 100)
solution5 = collider_angulation(0, 500, 10, 100)
solution6 = collider_angulation(0, 600, 10, 100)
solution7 = collider_angulation(0, 700, 10, 100)
solution8 = collider_angulation(0, 800, 10, 100)

plt.plot(solution0[0][:], solution0[1][:], label='(0,0)')
plt.plot(solution1[0][:], solution1[1][:], label='(0,100)')
plt.plot(solution2[0][:], solution2[1][:], label='(0,200)')
plt.plot(solution3[0][:], solution3[1][:], label='(0,300)')
plt.plot(solution4[0][:], solution4[1][:], label='(0,400)')
plt.plot(solution5[0][:], solution5[1][:], label='(0,500)')
plt.plot(solution6[0][:], solution6[1][:], label='(0,600)')
plt.plot(solution7[0][:], solution7[1][:], label='(0,700)')
plt.plot(solution8[0][:], solution8[1][:], label='(0,800)')
plt.legend()
plt.grid()
plt.show()

plt.plot(solution0[0][:], solution0[2][:], label='(0,0)')
plt.plot(solution1[0][:], solution1[2][:], label='(0,100)')
plt.plot(solution2[0][:], solution2[2][:], label='(0,200)')
plt.plot(solution3[0][:], solution3[2][:], label='(0,300)')
plt.plot(solution4[0][:], solution4[2][:], label='(0,400)')
plt.plot(solution5[0][:], solution5[2][:], label='(0,500)')
plt.plot(solution6[0][:], solution6[2][:], label='(0,600)')
plt.plot(solution7[0][:], solution7[2][:], label='(0,700)')
plt.plot(solution8[0][:], solution8[2][:], label='(0,800)')
plt.legend()
plt.grid()
plt.show()

plt.plot(solution0[1][:], solution0[2][:], label='(0,0)')
plt.plot(solution1[1][:], solution1[2][:], label='(0,100)')
plt.plot(solution2[1][:], solution2[2][:], label='(0,200)')
plt.plot(solution3[1][:], solution3[2][:], label='(0,300)')
plt.plot(solution4[1][:], solution4[2][:], label='(0,400)')
plt.plot(solution5[1][:], solution5[2][:], label='(0,500)')
plt.plot(solution6[1][:], solution6[2][:], label='(0,600)')
plt.plot(solution7[1][:], solution7[2][:], label='(0,700)')
plt.plot(solution8[1][:], solution8[2][:], label='(0,800)')
plt.legend()
plt.grid()
plt.show()