function a = thresholding(pixels, limit)
  a = (pixels >= limit).*255;