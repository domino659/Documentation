import shutil
from glob import glob
import os

from PIL import Image

image_dir = "images"
images = glob(f"{image_dir}/*.*")

for im in images:
    largeur = Image.open(im).size[0]

    if largeur < 250:
        destination = os.path.join(image_dir, "small")
    elif largeur < 500:
        destination = os.path.join(image_dir, "medium")
    elif largeur < 1000:
        destination = os.path.join(image_dir, "large")
    else:
        destination = os.path.join(image_dir, "extra-large")

    shutil.copy(im, destination)
