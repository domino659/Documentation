from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

im = Image.open("../../_images/ville.jpg")
font_path = "../../_utils/roboto.ttf"


def copyright(image, texte, opacity=1.0, rotation=30):
    image = image.convert("RGBA")
    texte_image = Image.new("RGBA", image.size, (255, 255, 255, 0))

    fontsize = 1
    font = ImageFont.truetype(font_path, fontsize)
    while font.getsize(texte)[0] < image.size[0]:
        fontsize += 1
        font = ImageFont.truetype(font_path, fontsize)

    text_height = font.getsize(texte)[1]
    pos = (0, (image.size[1] / 2) - (text_height / 2))

    d = ImageDraw.Draw(texte_image)
    d.text(pos, texte, fill=(255, 255, 255, round(opacity * 255)), font=font)

    texte_image = texte_image.rotate(rotation)

    return Image.alpha_composite(image, texte_image)



im_copyright = copyright(im, "Thibault", opacity=0.5, rotation=-30)
im_copyright.show()



