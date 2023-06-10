from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq, rfft, rfftfreq
import numpy as np

#C:\Users\1\Documents\практика\звуки\fonoteca-raskat-groma.wav тестовый звук
import scipy.optimize as opt
#входные данные - файл и диапазон частот
filename=input()
a, b = wavfile.read(filename, mmap=int) 
b=np.int16(b/b.max()*32767)
def srez(r, down, up): 
	jup=0
	jdown=0
	for i in  range(r.size):
		if r[i]<=up:
			jup=i
		else:
			break
	for i in range(r.size-1, -1, -1):
		if r[i]>=down:
			jdown=i
		else:
			break	
	return jdown, jup
y1=[]
x1=np.array([550, 750, 925, 1125, 1325, 1525, 1725, 1925, 2125, 2325, 2525])
mass=[[500, 600],[700, 800],[900, 950],[1100, 1150],[1300, 1350],[1500, 1550],[1700, 1750],[1900, 1950],[2100, 2150],[2300, 2350],[2500, 2550]]
for i in mass:
	n, v=i[0], i[1]
	#высчитываем среднюю мощность
	it=[] 
	t=0
	while t+10000<b.size:
		mass=b[t:t+10000]
		y=np.abs(rfft(mass))
		x=rfftfreq(y.size, 1/a )
		down, up=srez(x, n, v)
		if up!=down:
			sr=np.sum(y[down:up])/(up-down)
			it.append(sr)
		t+=10000
	it=np.array(it)
	xit=np.arange(5000/a, (t+5000)/a, 10000/a)
	#подбираем подходящую функцию
	def func(x, A, c): #d=0 с<0
		return A*np.exp(c*x)
	x_lin = np.linspace(0, xit.max(), 50)
	p0 = [7000000, -2]	
	w, _ = opt.curve_fit(func, xit, it, p0=p0)
	y1.append(abs(w[1]))
	print(w[1])
	#выводим все на график
y1=np.array(y1)
plt.scatter(x1, y1, s=1)
plt.xlabel('частоты')
plt.ylabel('коэффициент')
plt.show()