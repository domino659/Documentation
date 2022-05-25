from PIL import Image

from _utils import compare

image = Image.open("../../_images/ville.jpg")
gradient = Image.open("../../_images/degrade.png")

gradient = gradient.resize(image.size).transpose(Image.FLIP_TOP_BOTTOM)

images = []
for i in range(1, 5):
    im_filtre = Image.blend(image, gradient, i / 10)
    images.append(im_filtre)

compare(*images)
