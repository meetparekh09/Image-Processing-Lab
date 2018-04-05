function fr = bitSlicing(f, bit)
  for i = 1:rows(f)
    for j = 1:columns(f)
      if(!(f(i, j) > 2^(bit-1) - 1 && f(i, j) < 2^bit))
        f(i, j) = 0;
      endif
    endfor
  endfor
  fr = f;        