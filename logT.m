function l = logT(f)
  f = log(f);
  l = uint8((f./max(max(f))).*255);