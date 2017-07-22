from PIL import Image, ImageDraw
import math, itertools

im = Image.open('geez3.jpg')# im = Image.new('RGBA', (400, 400), (0, 255, 0, 0))

draw = ImageDraw.Draw(im,'RGBA')
r = 1
x = 0
y = 0
n = 10
s = 500
store = []
im2 = Image.new("RGBA", (s, s), (0,0,0,0))
draw2 = ImageDraw.Draw(im2,'RGBA')
for i in range(n):
    print(' ')
    #draw.ellipse((s / (n - 1) * i - r, y - r, s / (n - 1) * i + r, y + r), fill = (255, 0, 0, 1))
    
    #draw.ellipse((y - r, s / (n - 1) * i - r, y + r, s / (n - 1) * i + r), fill = (255, 0, 0, 1))
    
    #draw.ellipse((s / (n - 1) * i - r, s + y - r, s / (n - 1) * i + r, s + y + r), fill = (255, 0, 0, 1))
    
    #draw.ellipse((s + y - r, s / (n - 1) * i - r, s + y + r, s / (n - 1) * i + r), fill = (255, 0, 0, 1))
    
    
    a = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.')
    b = str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
    c = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.')
    d = str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
    
    #print(a)
    #print(b)
    #print(c)
    #print(d)
    
    if a not in store:
        store.append(a)
    else:
        print(a)
    if b not in store:
        store.append(b)
    else:
        print(b)
    if c not in store:
        store.append(c)
    else:
        print(c)
    if d not in store:
        store.append(d)
    else:
        print(d)

print(len(store))

store2 = [[float(y) for y in x.split()] for x in store]
store3 = [[z[0]/2+z[1]/2,z[2]/2+z[3]/2] for z in store2]
store4 = list(reversed([[z[0]/2+z[1]/2,z[2]/2+z[3]/2] for z in store2]))

#draw2.line((0, im.size[1], im.size[0], 0), fill=(100,100,100,255))



def rec_line(l):
    print(l)
    if len(l) > 2:
        first_item = l[0]
        l2 = l[1:]
        
        for pos in l2:
            sw = [first_item[0],first_item[1],pos[0],pos[1]]
            
            
                    
            filler = (round(first_item[0]),round(first_item[1]),round(pos[1]),255)
            draw2.line(tup, fill=filler)
        rec_line(l2)
    else:
        draw2.line((l[0][0],l[0][1],l[1][0],l[1][1]), fill=(0,0,0,0))
        
rec_line(store3)
#for i in range(len(store3)):
    #for j in range(len(store3)):
        #tup = (store3[i][0],store3[i][1],store4[j][0],store4[j][1])
        #filler = (round(store3[j][1]),round(store3[i][0]),round(store3[j][1]),255)
        #print(tup)
        #draw2.line(tup, fill=filler)
    
im2.show()
im2.save('a.png')
