function a = sine()
  x = 0:10:720;
  x = x.*(pi/180);
  y = sin(x);
  figure('name', 'Sine Wave');
  plot(x, y);
  a = 1;