import numpy as np
import os

from skimage.io import imread, imsave
from skimage.color import rgb2gray
from skimage import img_as_ubyte

from font_area import mean_brightness_dict

img_path = '.\img'

images = os.listdir(img_path)

grey_scale_images = []

for image in images:
    temp_image = rgb2gray(imread(os.path.join(img_path, image))[:,:,0:3])
    grey_scale_images.append(np.round(img_as_ubyte(temp_image)/255,3))

for img, name in zip(grey_scale_images, images):
    result = np.array([[mean_brightness_dict[brightness] for brightness in row] for row in img])
    np.savetxt(os.path.join('output', name[:-4]+'.txt'), result, delimiter='', fmt='%s')