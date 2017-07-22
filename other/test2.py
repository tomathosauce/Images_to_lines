from PIL import Image, ImageDraw


s = 500
b = s*10/100

im = Image.new("RGB", (s, s), (0,0,0))
draw = ImageDraw.Draw(im,'RGBA')

draw.rectangle((b,b,s-b,s-b),outline=(255,255,255,255),fill=(255,255,255,50))

im.show()
