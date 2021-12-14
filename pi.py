import matplotlib.pyplot as plt
from matplotlib import animation
import random as rnd
import math

def setplot1(sx,sy):
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([-sx,sx])
	plt.ylim([-sy,sy])
	ax.set_facecolor('xkcd:black')

def setplot2(sx1,sx2,sy1,sy2):
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([sx1,sx2])
	plt.ylim([sy1,sy2])
	ax.set_facecolor('xkcd:black')


frps=60
sec=3*60

fig, a=plt.subplots()
N=1000
nr=0
nb=0
per='%'

def run(frame):
	global nr,nb
	for i in range(N):
		x=rnd.random()
		y=rnd.random()
		if math.sqrt(x**2+y**2)<=1:
			plt.plot([x],[y],'ro',markersize=1)
			nr+=1
		else:
			plt.plot([x],[y],'bo',markersize=1)
			nb+=1
	pi=4*nr/(nr+nb)
	plt.suptitle(r'$\pi \approx$ %f' % pi)
	pe=100*abs(pi-math.pi)/math.pi
	plt.title(per+'Error = %f' % pe)
	setplot2(0,1,0,1)

ani=animation.FuncAnimation(fig,run,frames=frps*sec)
writervideo=animation.FFMpegWriter(fps=frps)
ani.save('pi_est.mp4', writer=writervideo)
plt.show()
