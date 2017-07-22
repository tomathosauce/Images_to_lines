from PIL import Image, ImageDraw, ImageChops
import math, time
im = Image.open('geez3.jpg')# im = Image.new('RGBA', (400, 400), (0, 255, 0, 0))

white = (255,255,255,120)
red = (255,0,0,160)
r = 5
x = 0
y = 0
n = 5
s = 363
store = []
im2 = Image.new("RGB", (s, s), (0,0,0,255))
draw2 = ImageDraw.Draw(im2,'RGBA')


test_point = [40,70]
bound = 1
#i = 50

#draw2.ellipse((s / (n - 1) * i - r, y - r, s / (n - 1) * i + r, y + r), fill = (255, 0, 0, 255))


for i in range(n):
    print(' ')
    #draw2.ellipse((s / (n - 1) * i - r, y - r, s / (n - 1) * i + r, y + r), fill = (255, 0, 0, 255))
    
    #draw2.ellipse((y - r, s / (n - 1) * i - r, y + r, s / (n - 1) * i + r), fill = (255, 0, 0, 1))
    
    #draw2.ellipse((s / (n - 1) * i - r, s + y - r, s / (n - 1) * i + r, s + y + r), fill = (255, 0, 0, 1))
    
    #draw2.ellipse((s + y - r, s / (n - 1) * i - r, s + y + r, s / (n - 1) * i + r), fill = (255, 0, 0, 1))
    
    storage = [s / (n - 1) * i - r]
    
    top_ = []
    left_ = []
    right_ = []
    bottom_ = []
    
    a = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.')
    b = str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
    c = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.')
    d = str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
    
    st = [a,b,c,d]
    
    for ele in st:
        if ele not in store:
            print(ele)
            print('printed')
            store.append(ele)
            
    print('\n\n\n')
    print('end')

print(len(store))
print(store)
print('\n\n\n')

store2 = [[float(y) for y in x.split()] for x in store]
store3 = [[z[0]/2+z[2]/2,z[1]/2+z[3]/2] for z in store2]

print(store2)
print('\n\n\n')
print(store3)
print('\n\n\n')

#draw2.line((0, im.size[1], im.size[0], 0), fill=(100,100,100,255))



count = 0

store5 = []

for pos in store3:
    for pos2 in store3:
        arr = pos+pos2
        if [arr[2],arr[3],arr[0],arr[1]] not in store5:
            
            if (pos[0] != pos2[0] and pos[1] != pos2[1] )or (pos2[1]<s and pos2[0]<s and pos[0]>0 and pos[1]>0):
                count=count+1
                print(pos[0] != pos2[0])
                print('\n')
                print(pos[1] != pos2[1])
                print('\n')
                print(tuple(pos+pos2))
                print('\n')
            
                draw2.line(tuple(pos+pos2),fill=white)
                store5.append(pos+pos2)
                
im2.show()
print(store5)
print(len(store5))
#im2.save(str(store5.index(coor))+'.png')

print(count)
print(len(list(im.getdata())))
#im2.save('d.png')
