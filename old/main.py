from PIL import Image, ImageDraw, ImageChops
import math, time
import functions as funcs

im = Image.open('geez3.jpg')# im = Image.new('RGBA', (400, 400), (0, 255, 0, 0))

white = (255,255,255,120)

#draw = ImageDraw.Draw(im,'RGB')

r = 5
x = 0
y = 0
n = 70
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
        
#rec_line(store3)

store5 = []



for pos in store3:
    for pos2 in store3:
        if pos[0] != pos2[0] and pos[1] != pos2[1]:
            arr = pos+pos2
            
            if [arr[2],arr[3],arr[0],arr[1]] not in store5:
                count=count+1
                print('\n\n\n')
                print(pos[0] != pos2[0])
                print('\n\n\n')
                print(pos[1] != pos2[1])
                print('\n\n\n')
                print(tuple(pos+pos2))
                print('\n\n\n')
            
                #draw2.line(tuple(pos+pos2),fill=(round(pos[0]),round(pos[1]),round(pos2[1]),30))
                store5.append(pos+pos2)
            elif pos2[1]<s and pos2[0]<s and pos[0]>0 and pos[1]>0:
                
                
            
print(len(store5))

#draw2.ellipse((test_point[0]-bound, test_point[0]+bound, test_point[1]-bound, test_point[1]+bound), fill=(255,0,0,255))

valid_lines = []

for li in store5:
    slope = (li[1]-li[3])/(li[0]-li[2])
    b_component = li[1]-slope*li[0]
    test_line = test_point[0]*slope+b_component
    print(li)
    print(slope)
    print(b_component)
    print(test_line)
    print(test_point)
    if test_line > test_point[1]-bound and test_line < test_point[1]+bound:
        #draw2.line(tuple(li),fill=white)
        valid_lines.append(li)

def get_rgb_av(tup):
    return (tup[0]+tup[1]+tup[2])/3

canv = im2.copy()
dcanv = ImageDraw.Draw(canv,'RGBA')
o_pos = tuple(test_point)
fixed_pix = im2.getpixel(o_pos)

start = time.time()

for line in valid_lines:
    line_copy = im2.copy()
    new_draw = ImageDraw.Draw(line_copy,'RGBA')
    
    
    new_draw.line(tuple(line),fill=white)
    
    #dcanv.line(tuple(line),fill=white)
    
    
    #dat = list(im2.getdata())
    #dat2 = list(line_copy.getdata())
    
    #pos = test_point[0]*test_point[1]
    
    
    
    print(line_copy.getpixel(tuple(test_point)))
    
    #print(dat[pos])
    #print(dat2[pos])
    
    if line_copy.getpixel(o_pos) != fixed_pix:
    #if dat[pos] != dat2[pos]:
        line_copy.show()

#im2.save(str(store5.index(coor))+'.png')

print(count)
canv.show()
end = time.time()
print(len(list(im.getdata())))
print('Valid Lines: '+str(len(valid_lines)))
print('Time it took to run: '+str(round(end - start))+' s')
#im2.save('d.png')
