import textwrap
from random import randint

from PIL import Image, ImageDraw, ImageFont

# point to the font to use
font = ImageFont.truetype("/Users/lreding/Library/Fonts/NHaasGroteskTXPro-65Md.ttf", 90)

cols = [
    "#5E5A6E",
    "#1F1B29",
    "#b33f62",
    "#8A0E38",
    "#CC503E",
    "#e39d25",
    "#C0392B",
    "#336E7B",
    "#16A085",
]

width, height = 2650, 1600

with open("quotes.txt", "r") as file:
    for i, line in enumerate(file):
        if i < 30:
            if line != "\n" and line.find(":::") != -1:
                try:
                    # generate random col
                    col = randint(0, len(cols) - 1)

                    quote, name, *_ = line.split(":::")

                    quote_wrapped = textwrap.fill(quote.capitalize(), 50)
                    quote_with_author = (
                        quote_wrapped + "\n\n" + name.strip().replace(".", "")
                    )

                    img = Image.new("RGBA", (width, height), cols[col])
                    draw = ImageDraw.Draw(img)

                    draw.text((10, 1000), quote_with_author, (255, 255, 255), font=font)
                    draw = ImageDraw.Draw(img)
                    img.save("{}.png".format(quote_wrapped[:10].replace(" ", "_")))

                except Exception as e:
                    print(f"problem with line {i}: {e}")
