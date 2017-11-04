import PIL
from PIL import ImageFont, Image, ImageOps, ImageDraw
import os
import re
from random import randint


font = ImageFont.truetype("/Users/lreding/Library/Fonts/NHaasGroteskTXPro-65Md.ttf", 90)

cols = ['#5E5A6E', '#1F1B29', '#b33f62', '#8A0E38', '#CC503E', '#e39d25', '#C0392B', '#336E7B', '#16A085']

width, height = 2650, 1600

filename = "quotes.txt"

counter = 0

with open(filename, 'r') as file:
    for i, line in enumerate(file):
        if counter < 30:
            if line != "\n":
                try:
                    # generate random col
                    col = randint(0, len(cols)-1)

                    quote, name, *_ = line.split(":::")

                    if len(quote) < 100:

                        img = Image.new("RGBA", (width, height), cols[col])
                        draw = ImageDraw.Draw(img)

                        # wrap long quotes
                        x = '\n'.join(line.strip() for line in re.findall(r'.{1,40}(?:\s+|$)', quote))
                        x += "\n- {}".format(name.split('.')[0])
                        draw.text((10, 1000), x.capitalize(), (255,255,255), font = font)
                        draw = ImageDraw.Draw(img)
                        img.save("{}.png".format(x[:10]))
                        counter += 1
                except:
                    print("problem with line {}".format(i))
