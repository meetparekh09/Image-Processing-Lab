function a = histogramEqualization(img)
  p = size(img)(1)*size(img)(2);
  y_bef = zeros(1, 256);
  x = 0:255;
  for i = 1:p
    y_bef(img(i)+1) += 1;
  endfor
  figure;
  bar(x, y_bef);
  axis([0 255]);
  figure;
  title('Image Before');
  imshow(img);
  df = y_bef./p;
  sum = 0;
  cdf = zeros(1, 256);
  for i = 1:256
    sum += df(i);
    cdf(i) = sum;
  endfor
  equ_img = img;
  for i = 1:p
    equ_img(i) = round(cdf(img(i)+1)*255);
  endfor
  y_af = zeros(1, 256);
  for i = 1:p
    y_af(equ_img(i)+1) += 1;
  endfor
  figure;
  bar(x, y_af);
  axis([0 255]);
  figure;
  imshow(equ_img);
  title('Image After');
  a = 1;