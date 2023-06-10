from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq, rfft, rfftfreq
import numpy as np
import scipy.optimize as opt
#входные данные - файл и диапазон частот
filename=input()
a, b = wavfile.read(filename, mmap=int) 
n, v=map(int, input().split())
#высчитываем среднюю мощность
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

it=[] 
t=10000
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
xit=np.arange(5000/a, (t-5000)/a, 10000/a)
#подбираем подходящую функцию
def func(x, A, c): #d=0 с<0
    return A*np.exp(c*x)
x_lin = np.linspace(0, xit.max(), 50)
p0 = [7000000, -2]	
w, _ = opt.curve_fit(func, xit, it, p0=p0)
y_model = func(x_lin, *w)
print(*w)
#выводим все на график
#plt.plot(x_lin, y_model)
plt.scatter(xit, it, s=1)
plt.plot(x_lin, y_model, "k--")
#plt.scatter(xit, it, s=1)
plt.xlabel('время, с')
plt.ylabel('средняя интенсивность волн с ч-той от '+str(n)+' до '+str(v)+' Гц ')
plt.show()