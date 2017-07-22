from PIL import Image, ImageDraw, ImageChops
import math, time, numpy

im = Image.open('geez3.jpg')
# im = Image.new('RGBA', (400, 400), (0, 255, 0, 0))
s = 363

im3 = im.copy()
im3.convert('RGB')
white = (255,255,255,250)
red = (255,0,0,120)
im2 = Image.new("RGB", (s, s), (0,0,0,255))
im2.paste(im)
#im2.show()
#draw = ImageDraw.Draw(im,'RGB')

dim2 = ImageDraw.Draw(im2,'RGBA')
dim2.line((0,0,363,363),fill=white)
#im2.show()
im3.show()
start = time.time()

diff = ImageChops.difference(im3.convert('L'),im2.convert('L'))
arr = im3.convert('L')
arr = list(arr.getdata())
arr2 = im2.convert('L')
arr2 = list(arr2.getdata())

st = []

for i in range(len(arr)):
    if arr[i] != arr2[i]:
        st.append(arr2[i]-arr[i])

print(numpy.mean([x for x in list(diff.getdata()) if x != 0]))

end = time.time()

print(end-start)
print(st)
diff.show()
