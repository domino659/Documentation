from PIL import Image

# Exercice 01
im1 = Image.open("rose.jpg")
im1.rotate(45, fillcolor="green").save("rose-rotate.jpg")

# Exercice 02
im2 = Image.open("homme.png")
im_finale = Image.new("RGB", im2.size, color="green")
im_finale.paste(im2, im2)
im_finale.save("homme-vert.jpg")
im_finale.show()
