from PIL import Image, ImageDraw
import math

image = Image.open('geez3.jpg')
maxsize = (500, 500)
image = image.resize(maxsize, Image.ANTIALIAS)

image.save('resized_geez.jpg')
