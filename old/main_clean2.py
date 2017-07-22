from PIL import Image, ImageDraw, ImageChops, ImageOps
import math, time, numpy

im = Image.open('geez3.jpg')
start = time.time()

r = 5
x = 0
y = 0
n = 10
 
s = im.width
bound = 1
palette = {
    'white' : (255,255,255,15),
    'red' : (255,0,0,120),
    'black' : (0,0,0,15)
}

pic = Image.new("RGB", (s, s), (0,0,0,255))
pic.paste(im)
#print(pic.getpixel((164,12)))
store = []
my_canvas = Image.new("RGB", (s, s), (255,255,255,255))
draw_my_canvas= ImageDraw.Draw(my_canvas,'RGBA')
my_canvas_copy = my_canvas.copy()
draw_my_canvas_copy= ImageDraw.Draw(my_canvas_copy,'RGBA')


for i in range(n):
    a = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.')
    b = str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
    c = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.')
    d = str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
    
    st = [a,b,c,d]
    
    for ele in st:
        if ele not in store:
            store.append(ele)

darkest_pixel = pic.convert('L')
darkest_pixel = list(darkest_pixel.getdata())
print(darkest_pixel)
darkest_pixel = darkest_pixel.index(min(darkest_pixel))
print(darkest_pixel)
darkest_pixel = (round(darkest_pixel%s),round((darkest_pixel-(darkest_pixel%s))/s))
print(darkest_pixel)

store2 = [[float(y) for y in x.split()] for x in store]
store3 = [[z[0]/2+z[2]/2,z[1]/2+z[3]/2] for z in store2]
count = 0
store5 = []
for pos in store3:
    for pos2 in store3:
        arr = pos+pos2
        if [arr[2],arr[3],arr[0],arr[1]] not in store5:
            if (pos[0] != pos2[0] and pos[1] != pos2[1]) or (pos2[1]<s and pos2[0]<s and pos[0]>0 and pos[1]>0):
                count=count+1
                
                print(pos+pos2)
                #draw2.line(tuple(pos+pos2),fill=(round(pos[0]),round(pos[1]),round(pos2[1]),30))
                store5.append(pos+pos2)
                
            
print('Store5 length: '+str(len(store5)))
print('Store2 length: '+str(len(store2)))

'''
valid_lines = []

o_pos = darkest_pixel
fixed_pix = pic.getpixel(o_pos)

canv = pic.copy()
draw_canv = ImageDraw.Draw(canv,'RGBA')

for li in store5:
    if li[0]-li[2] != 0:
        slope = (li[1]-li[3])/(li[0]-li[2])
        b_component = li[1]-slope*li[0]
        test_line = darkest_pixel[0]*slope+b_component
    
        if test_line > darkest_pixel[1]-bound and test_line < darkest_pixel[1]+bound:
            line_copy = pic.copy()
            new_draw = ImageDraw.Draw(line_copy,'RGBA')
            new_draw.line(tuple(li),fill=palette['white'])
            draw_canv.line(tuple(li),fill=palette['white'])
            draw_my_canvas.line(tuple(li),fill=palette['black'])
            print(line_copy.getpixel(o_pos))
            print(fixed_pix)
            
            if line_copy.getpixel(o_pos) != fixed_pix:
                bw_copy = line_copy.convert('L')
                o_copy = pic.convert('L')
                
                
                
                diff = ImageChops.difference(bw_copy,o_copy)
                score = numpy.mean([x for x in list(diff.getdata()) if x != 0])
                
                print(score)
                
                valid_lines.append([li,score])
                #line_copy.show()
    elif li[0] == darkest_pixel[0] and li[0]-li[2] == 0:
        line_copy = pic.copy()
        new_draw = ImageDraw.Draw(line_copy,'RGBA')
        new_draw.line(tuple(li),fill=palette['white'])
        bw_copy = line_copy.convert('L')
        o_copy = pic.convert('L')
        diff = ImageChops.difference(bw_copy,o_copy)
        score = numpy.mean([x for x in list(diff.getdata()) if x != 0])
        valid_lines.append([li,score])
        
canv.show()
my_canvas.show()
print(fixed_pix)
sorted_lines = sorted(valid_lines, key=lambda e: e[1], reverse=True)
print(sorted_lines)
if len(sorted_lines) > 0:
    draw_my_canvas_copy.line(tuple(sorted_lines[0][0]),fill=palette['black'])

border = ImageOps.expand(pic,5,fill=(255,255,255,255))
print(border.height)
border.show()
my_canvas_copy.show()
draw_pic = ImageDraw.Draw(pic,'RGBA')

for l in store5:
    draw_pic.line(tuple(l),fill=palette['white'])
    
pic.show()
print(count)
end = time.time()
print(len(list(im.getdata())))
print('Valid Lines: '+str(len(valid_lines)))
print('Time it took to run: '+str(round(end - start))+' s')
'''
