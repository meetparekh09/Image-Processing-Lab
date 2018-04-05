from PIL import Image
import scipy.fftpack
import numpy as np
dct, idct = scipy.fftpack.dct, scipy.fftpack.idct
quantization_matrix = [16, 11, 10, 16, 24, 40, 51, 61, 12, 12, 14, 19, 26, 58, 60, 55, 14, 13, 16, 24, 40, 57, 69, 56, 14, 17, 22, 29, 51, 87, 80, 62, 18, 22, 37, 56, 68, 109, 103, 77,24, 35, 55, 64, 81, 104, 113, 92, 49, 64, 78, 87, 103, 121, 120, 101, 72, 92, 95, 98, 112, 100, 103, 99]
quantization_matrix = np.array(quantization_matrix).reshape(8,8)
def _blockshaped(pixels, nrows=8, ncols=8):
	h, w = pixels.shape
	return (pixels.reshape(h//nrows, nrows, -1, ncols).swapaxes(1,2).reshape(-1, nrows, ncols))
def _unblockshaped(pixels, h, w):
	n, nrows, ncols = pixels.shape
	return (pixels.reshape(h//nrows, -1, nrows, ncols).swapaxes(1,2).reshape(h, w))
def compress(pixels):
	height, width, c = pixels.shape
	color = np.dsplit(pixels, 3)[0].reshape(height, width)
	h_pad, w_pad = height % 8, width % 8
	if h_pad > 0:
		h_pad = 8 - h_pad
	if w_pad > 0:
		w_pad = 8 - w_pad
	padded_height, padded_width = height + h_pad, width + w_pad
	padded_color = np.zeros((padded_height, padded_width))[:height, :width] = color
	subImages = _blockshaped(padded_color)
	subImages -= 128
	subImages_dct = dct(dct(subImages, norm='ortho', axis=2), norm='ortho', axis=1)
	quantized_subimages_dct = np.round(subImages_dct/quantization_matrix)
	return (quantized_subimages_dct, height, width, h_pad, w_pad)
def decompress(compressedImage):
	quantized_subimages_dct, height, width, h_pad, w_pad = compressedImage
	subImages_dct = quantized_subimages_dct * quantization_matrix
	subImages = idct(idct(subImages_dct, norm='ortho', axis=1), norm='ortho', axis=2)
	subImages += 128
	pixels = _unblockshaped(subImages, height+h_pad, width+w_pad)
	pixels = pixels[:height, :width]
	pixels = np.abs(pixels)
	pixels[pixels > 255] = 255
	return (np.dstack((pixels, pixels, pixels))).astype(np.uint8)
def error(pixels, jpeg_pixels):
	return np.abs(pixels - jpeg_pixels).astype(np.uint8)
image = Image.open('Images/qDvrs.jpg')
pixels = np.array(image, dtype=np.int64)
compressedImage = compress(pixels)
jpeg_pixels = decompress(compressedImage)
new_image = Image.fromarray(jpeg_pixels, "RGB")
new_image.show()
error_image = Image.fromarray(error(pixels, jpeg_pixels), "RGB")
error_image.show()
