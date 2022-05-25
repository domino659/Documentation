from PIL import Image

from _utils import compare

im = Image.open("../../_images/rose.jpg")

im1 = im.split()[0]
im2 = im.split()[1]
im3 = im.split()[2]
im4 = im.convert("L")

compare(im1, im2, im3, im4)
