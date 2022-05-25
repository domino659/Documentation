from PIL import Image
from glob import glob
import os

from _utils import compare

images = glob("*.jpg")

for image in images:
    im = Image.open(image)
    couches = im.split()
    im_comparaison = compare(*couches)
    filename, ext = os.path.splitext(image)
    im_comparaison.save(f"{filename}-comparaison{ext}")
