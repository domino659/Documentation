from PIL import Image
from PIL import ImageEnhance

from _utils import compare

im = Image.open("../../_images/portrait.jpg")

images = []

for i in range(5, 25, 5):
    im_filtre = ImageEnhance.Brightness(im).enhance(i / 10)
    images.append(im_filtre)

compare(*images)
