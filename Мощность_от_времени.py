from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq, rfft, rfftfreq
import numpy as np
import scipy.optimize as opt
#входные данные
filename=input()
a, b = wavfile.read(filename, mmap=int)
b=np.int16(b/b.max()*32767) 
#обрабатываем данные
it=[] 
t=0
while t+10000<b.size:
	mass=b[t:t+10000]
	y=np.abs(rfft(mass))
	r=y.sum()
	it.append(r)
	t+=10000
it=np.array(it)
xit=np.arange(5000/a, (t+5000)/a, 10000/a)
#ищем коэффициэнты
def func(x, A, c, k): #d=0 с<0
    return A*(np.exp(c*x))+k*x**(-2)
x_lin = np.linspace(0, xit.max(), 50)
p0 = [7000000, -2, 100]	
w, _ = opt.curve_fit(func, xit, it, p0=p0)
y_model = func(x_lin, *w)
print(*w)
#выводим все на график
plt.semilogy(x_lin, y_model)
plt.semilogy(xit, it)
#plt.plot(x_lin, y_model, "k--")
#plt.scatter(xit, it, s=1)
plt.xlabel('время, с')
plt.ylabel('интенсивность')
plt.show()


