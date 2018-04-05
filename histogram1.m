function fr = histogram1(f)
  fr = zeros(1, 256);
  for i = 1:rows(f)
    for j = 1:columns(f)
      fr(f(i, j) + 1) = fr(f(i, j) + 1) + 1;
    end
  end