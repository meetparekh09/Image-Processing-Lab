function fr = contrastStrecthing(f, in, out)
  f = double(f);
  f = (f - in(1)).*((out(2) - out(1))/ (in(2) - in(1))) + out(1);
  fr = uint8(f);