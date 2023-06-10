from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq, rfft, rfftfreq
import numpy as np

filename=input()
a, b = wavfile.read(filename, mmap=int) 
b=b[4*a:4*a+a//2]
yf=rfft(b) 

xf=rfftfreq(b.size, 1/a )

yf=np.abs(yf)

s=yf.sum()

def srez(r, up, down): #r-кусок отfftшной функции up-макс ч-та down- мин ч-та
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
	return jup, jdown

plt.semilogy(xf, yf)
plt.xlabel('частота, Гц')
plt.ylabel('интенсивность')
plt.show()

