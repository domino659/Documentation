from PIL import Image

im = Image.open("../../_images/rose.jpg")
im.thumbnail((250, 250))
im.save("../../_images/rose-small.jpg")
