function a = rampSignal()
  x = -10:10;
  y = -10:10;
  y = (y >= 0).*y;
  figure('name', 'Ramp Signal');
  plot(x, y);
  axis([-10 10 -5 10]);
  a = 1;