from PIL import Image
from glob import glob
import os

facteurs = [2, 4]

images = glob("*.jpg")

for image in images:
    im = Image.open(image)

    for facteur in facteurs:
        x, y = im.size
        x_facteur, y_facteur = round(x / facteur), round(y / facteur)
        im_resize = im.resize((x_facteur, y_facteur))
        filename, ext = os.path.splitext(image)
        new_filename = f"vignettes/{filename}-{x_facteur}x{y_facteur}{ext}"
        im_resize.save(new_filename)
