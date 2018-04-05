function fr = intensitySlicing(f, in, out)
  if(rows(out) > 1)
    for i = 1:rows(f)
      for j = 1:columns(f)
        if(f(i, j) < in(1))
          f(i, j) = out(1);
        elseif(f(i, j) > in(2))
          f(i, j) = out(1);
        else
          f(i, j) = out(2);
        endif
      endfor
    endfor
  else
    for i = 1:rows(f)
      for j = 1:columns(f)
        if(f(i, j) >= in(1) && f(i, j) <= in(2))
          f(i, j) = out(1);
        endif
      endfor
    endfor
  endif
  fr = f; 