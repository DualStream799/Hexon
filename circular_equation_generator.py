diam_terra = 12.7562#10^6m
r_terra = diam_terra/2
alt_max = 0.353 #10^6m
alt_min = 0.340 #10^6m
a = r_terra + alt_max
b = r_terra + alt_min
a0 = [-a]
step = 0.001
time = np.arange(-a-step, a+step, step)


def planetary orbit(time, a, b):

	elip_list_pos = []
	elip_list_neg = []

	for x in time:
	    y_pos = b*((1 - (x**2/a**2))**(1/2))
	    y_neg = -y_pos
	    elip_list_pos.append(y_pos)
	    elip_list_neg.append(y_neg)

	    return [elip_list_pos, elip_list_neg]
