from PIL import Image
from PIL import ImageOps
from PIL import ImageEnhance

im = Image.open("../../_images/portrait.jpg").convert("L")

im = ImageOps.colorize(im, (255, 0, 0), (0, 255, 0), )
im = ImageEnhance.Contrast(im).enhance(3)
im = ImageEnhance.Color(im).enhance(0.5)
im.show()
