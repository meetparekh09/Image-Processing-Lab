import numpy as np
from PIL import Image

def alpha_trimmed_mean_filter(pixels, alpha, w_width, w_height):
	for i in range(0, w_width, pixels.shape[0]):
		for j in range(0, w_height, pixels.shape[1]):
			if (i+w_width < pixels.shape[0] and j+w_height < pixels.shape[1]):
				temp = pixels[i:i+w_width, j:j+w_height].reshape(w_width*w_height, 1)
				np.sort(temp)
				temp = temp[alpha/2:temp.shape[0]-(alpha/2)]
				pixels[i:i+w_width, j:j+w_height] = np.mean(temp)
	return pixels


if __name__ == "__main__":
	img = Image.open("Images/qDvrs.jpg")
	pixels = np.array(img)
	pixels = np.dsplit(pixels, 3)[0].reshape(pixels.shape[0], pixels.shape[1])
	atmf_pixels = alpha_trimmed_mean_filter(pixels, 4, 3, 3)
	atmf_pixels = np.dstack((atmf_pixels, atmf_pixels, atmf_pixels)).astype(np.uint8)
	new_img = Image.fromarray(atmf_pixels)
	new_img.show()