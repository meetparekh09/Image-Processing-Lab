import numpy as np
import matplotlib.pyplot as plt

def convolution(x, temp):
	x = np.hstack((np.array(x), np.zeros((len(temp) - 1))))
	temp = np.hstack((np.array(temp), np.zeros((len(x) - len(temp)))))
	conv = np.zeros(len(x))

	for i in range(len(conv)):
		for j in range(i+1):
			conv[i] += (x[j]*temp[i-j])
	return conv

def correlation(x,temp):
	x = np.array(x)
	temp = np.array(temp)
	len_x = len(x)
	len_temp = len(temp)
	t = np.zeros(2*len_x - 2 + len_temp)
	t[len_x - 1:len_x + len_temp - 1] = temp
	corr = np.zeros(len_temp + len_x - 1)

	for i in range(len(corr) - 1, -1, -1):
		corr[i] = np.sum(x * t[i:i + len_x])
	return corr

if __name__ == '__main__':
	first = [int(val) for val in raw_input("Signal 1 : ").split()]
	second = [int(val) for val in raw_input("Signal 2 : ").split()]
	cov = convolution(first, second)
	print("Convolution : " + str(cov))
	corr = correlation(first, second)
	print("Correlation : " + str(corr))
	x = range(len(first))
	plt.plot(x, first)
	plt.title('Signal 1')
	plt.show()
	x = range(len(second))
	plt.plot(x, second)
	plt.title('Signal 2')
	plt.show()
	x = range(len(cov))
	plt.plot(x, cov)
	plt.title('Convolution')
	plt.show()
	x = range(len(corr))
	plt.plot(x, corr)
	plt.title('Correlation')
	plt.show()