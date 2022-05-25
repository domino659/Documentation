from PIL import Image

im = Image.open("../../_images/rose.jpg")
im.transpose(Image.FLIP_LEFT_RIGHT)
im.transpose(Image.FLIP_TOP_BOTTOM)
im.transpose(Image.ROTATE_90)
im.rotate(95, fillcolor="red", expand=True)
