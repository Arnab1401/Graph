import numpy as np
import matplotlib as mpl

def linspace(start, stop, num=50, endpoint=True, retstep=False):
	num = int(num)
	if num <= 0:
		return array([], float)
	if endpoint:
		if num == 1:
			return array([float(start)])
		step = (stop-start)/float((num-1))
		y = np.arange(0, num) * step + start
		y[-1] = stop
	else:
		step = (stop-start)/float(num)
		y = np.arange(0, num) * step + start
	if retstep:
		return y, step
	else:
		return y
		
def complete_graph(n):
	x = cos(linspace(0,2*pi,n+1))
	y = sin(linspace(0,2*pi,n+1))
	for i in range(len(x)-1):
		for j in range(len(y)):
			mpl.pyplot.plot((x[i],x[j]),(y[i],y[j]))
