function a = laplaceTransform(img, weights)
  img = double(img);
  for i = 1:size(img)(1)
    for j = 1:size(img)(2)
      tot = 0;
      if (i-1>0 && i+1 <= size(img)(1))
        if(j+1 <= size(img)(2) && j-1 > 0)
          tot += sum(sum(img(i-1:i+1, j-1:j+1).*weights));
        elseif(j + 1 <= size(img)(2))
          tot += sum(sum(img(i-1:i+1, j:j+1).*weights(1:3, 2:3)));
        else
          tot += sum(sum(img(i-1:i+1, j-1:j).*weights(1:3, 1:2)));
        endif
      elseif (i+1 <= size(img)(1))
        if(j+1 <= size(img)(2) && j-1 > 0)
          tot += sum(sum(img(i:i+1, j-1:j+1).*weights(2:3, 1:3)));
        elseif(j + 1 <= size(img)(2))
          tot += sum(sum(img(i:i+1, j:j+1).*weights(2:3, 2:3)));
        else
          tot += sum(sum(img(i:i+1, j-1:j).*weights(2:3, 1:2)));
        endif
      else
        if(j+1 <= size(img)(2) && j-1 > 0)
          tot += sum(sum(img(i-1:i, j-1:j+1).*weights(1:2, 1:3)));
        elseif(j + 1 <= size(img)(2))
          tot += sum(sum(img(i-1:i, j:j+1).*weights(1:2, 2:3)));
        else
          tot += sum(sum(img(i-1:i, j-1:j).*weights(1:2, 1:2)));
        endif
      endif
      if (tot > 255)
        tot = 255;
      elseif(tot < 0)
        tot = 0;
      endif
      img(i, j) = img(i, j) - tot;
    endfor
  endfor
  img = uint8(img);
  a = img;