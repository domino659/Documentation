from PIL import Image

# Conversion simple
im = Image.open("../../_images/rose.jpg")
im.save("../../_images/rose.png")

# Conversion PNG à JPG
im = Image.open("../../_images/homme.png")
im.convert("RGB").save("../../_images/homme.jpg")

# Conversion avec modification de la couleur d'arrière plan
im = Image.open("../../_images/homme.png")
im_png = Image.new("RGB", im.size, (255, 0, 0))
im_png.paste(im, im)
im_png.save("../../_images/homme-bg-rouge.jpg")
