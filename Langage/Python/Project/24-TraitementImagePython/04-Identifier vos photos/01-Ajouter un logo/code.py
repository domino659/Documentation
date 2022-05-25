from PIL import Image

im = Image.open("../../_images/rose.jpg").convert("RGBA")
logo = Image.open("../../_images/logo_transp.png").convert("RGBA")


def copyright(image, position="hg", marge=20):
    largeur, hauteur = image.size
    logo_largeur, logo_hauteur = logo.size
    coord = {"hg": (0 + marge, 0 + marge),
             "bg": (0 + marge, hauteur - marge - logo_hauteur),
             "hd": (largeur - marge - logo_largeur, 0 + marge),
             "bd": (largeur - marge - logo_largeur, hauteur - marge - logo_hauteur)}

    image.paste(logo, coord.get(position), logo)
    image.show()


copyright(im, position="bd", marge=75)
