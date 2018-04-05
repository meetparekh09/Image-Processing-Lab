function fn = nthrootT(f, n)
  f = nthroot(f, n);
  fn = uint8((f./max(max(f))).*255);