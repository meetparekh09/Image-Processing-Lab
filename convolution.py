import numpy as np

def convolution(x, h):
	x = np.hstack((np.array(x), np.zeros(len(h)-1)))
	h = np.hstack((np.array(h), np.zeros(len(x)-len(h))))
	y = np.zeros(len(x))
	for i in range(len(y)):
		for j in range(i+1):
			y[i] += (x[j]*h[i-j])
	return y

def correlation(x, h):
	x = np.array(x)
	len_x = len(x)
	h = np.array(h)
	len_h = len(h)
	t = np.zeros(2*len_x - 2 + len_h)
	t[len_x - 1:len_x + len_h - 1] = h
	y = np.zeros(len_x+len_h-1)
	for i in range(len(y)-1, -1, -1):
		y[i] = np.sum(x*t[i:i+len_x])
	return y

if __name__ == "__main__":
	x = [int(val) for val in raw_input("Signal 1 : ").split()]
	h = [int(val) for val in raw_input("Signal 2 : ").split()]
	y = convolution(x, h)
	print "Convolution :: "
	print y
	y = correlation(x, h)
	print "\nCorrelation :: "
	print y