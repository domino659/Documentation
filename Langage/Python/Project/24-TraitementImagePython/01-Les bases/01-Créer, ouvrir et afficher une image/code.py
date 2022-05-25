from PIL import Image

# Création d'une nouvelle image
im = Image.new("RGBA", (1920, 1080), "#ff0000")
im.show()

# Ouverture d'une image sur le disque
im = Image.open("../../_images/rose.jpg")
im.show()
