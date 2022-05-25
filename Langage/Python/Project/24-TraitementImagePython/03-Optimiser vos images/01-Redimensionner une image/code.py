from PIL import Image

facteur = 2

im = Image.open("../../_images/rose.jpg")
t = im.size
t_reduit = (round(t[0] * facteur), round(t[1] * facteur))
im.resize(t_reduit).show()
