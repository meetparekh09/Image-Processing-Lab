function a = averageFilter(img, weights)
  [w_width, w_height] = size(weights);
  [img_width, img_height] = size(img);  
  img = im2double(img);
  for i = 1:w_width:(img_width - w_width)
    for j = 1:w_height:(img_height - w_height)
      img(i:i+w_width-1,j:j+w_height-1) = sum(sum((img(i:i+w_width-1,j:j+w_height-1).*weights)));
    end
  end
  img = im2uint8(img);
  a = img;
end