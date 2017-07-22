from PIL import Image, ImageDraw

s = 500

images = [Image.new("RGB", (s, s), (0,0,0,255)) for x in range(10)]
draw_images = [ImageDraw.Draw(x,'RGBA') for x in images]

for im in images:
    im.show()
