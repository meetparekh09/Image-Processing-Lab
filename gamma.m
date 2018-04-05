function fn = gamma(f, n)
  f = double(f).^n;
  fn = uint8((f./max(max(f))).*255);