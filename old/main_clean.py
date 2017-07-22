from PIL import Image, ImageDraw, ImageChops
import math, time, numpy
import functions as funcs

im = Image.open('geez3.jpg')
# im = Image.new('RGBA', (400, 400), (0, 255, 0, 0))

r = 5
x = 0
y = 0
n = 70
s = 363

pic = Image.new("RGB", (s, s), (0,0,0,255))
pic.paste(im)
pic.show()
white = (255,255,255,15)
red = (255,0,0,120)
black = (0,0,0,15)

#draw = ImageDraw.Draw(im,'RGB')


store = []
im2 = Image.new("RGB", (s, s), (0,0,0,255))
draw2 = ImageDraw.Draw(im2,'RGBA')


test_point = [40,70]
bound = 1

for i in range(n):
    a = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.')
    b = str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
    c = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.')
    d = str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
    
    st = [a,b,c,d]
    
    for ele in st:
        if ele not in store:
            store.append(ele)

store2 = [[float(y) for y in x.split()] for x in store]
store3 = [[z[0]/2+z[2]/2,z[1]/2+z[3]/2] for z in store2]
count = 0
store5 = []
for pos in store3:
    for pos2 in store3:
        if pos[0] != pos2[0] and pos[1] != pos2[1]:
            arr = pos+pos2
            
            if [arr[2],arr[3],arr[0],arr[1]] not in store5:
                count=count+1
                
                print(pos+pos2)
                #draw2.line(tuple(pos+pos2),fill=(round(pos[0]),round(pos[1]),round(pos2[1]),30))
                store5.append(pos+pos2)
                
            
print(len(store5))
valid_lines = []

o_pos = tuple(test_point)
fixed_pix = pic.getpixel(o_pos)

start = time.time()

for li in store5:
    slope = (li[1]-li[3])/(li[0]-li[2])
    b_component = li[1]-slope*li[0]
    test_line = test_point[0]*slope+b_component
    
    if test_line > test_point[1]-bound and test_line < test_point[1]+bound:
        line_copy = pic.copy()
        new_draw = ImageDraw.Draw(line_copy,'RGBA')
        new_draw.line(tuple(li),fill=white)
    
        if line_copy.getpixel(o_pos) != fixed_pix:
            bw_copy = line_copy.convert('L')
            o_copy = pic.convert('L')
            
            diff = ImageChops.difference(bw_copy,o_copy)
            score = numpy.mean([x for x in list(diff.getdata()) if x != 0])
            
            print(score)
            
            valid_lines.append([li,score])
            #comp = ImageChops.difference(line_copy,im2)
            #comp.show()
            #line_copy.show()



sorted_lines = sorted(valid_lines, key=lambda e: e[1], reverse=True))
print(count)
end = time.time()
print(len(list(im.getdata())))
print('Valid Lines: '+str(len(valid_lines)))
print('Time it took to run: '+str(round(end - start))+' s')
#im2.save('d.png')
