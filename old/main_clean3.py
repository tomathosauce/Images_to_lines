from PIL import Image, ImageDraw, ImageChops, ImageOps
import math, time, numpy

class snap():
    def __init__ (self, image, n_of_points, bound, border):
        #Open image
        self.image = Image.open(str(image))
        
        #Number of points per side of the image (preferably a square)
        self.n_of_points = n_of_points
        
        #Range where lines fall into
        self.bound = bound
        
        #Border thickness
        self.border = border
    
    def set_colors (self, kwargs**):
        self.colors = kwargs
        
    

#Radius of the circles, only if you were to draw them
r = 5

#Shift in the Y-axis
y = 0


n = 50

#Size of the image
s = im.width


bound = 1

#Borders
border = 5

#Colors
palette = {
    'white' : (255,255,255,15),
    'red' : (255,0,0,120),
    'black' : (0,0,0,15)
}

#The image to work with
pic = Image.new("RGB", (s, s), (0,0,0,255))
pic.paste(im)
pic = ImageOps.expand(pic, border, fill=(255,255,255,255))

#Store all positions
store = []

#Get all positions
for i in range(n):
    a = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.')
    b = str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
    c = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.')
    d = str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
    
    st = [a,b,c,d]
    
    for ele in st:
        if ele not in store:
            store.append(ele)

#Transform positions into a more usable format
store = [[float(y) for y in x.split()] for x in store]
store = [[z[0]/2+z[2]/2,z[1]/2+z[3]/2] for z in store]

#All possible lines
all_lines = []

#Get unrepeated lines
for pos in store:
    for pos2 in store:
        arr = pos+pos2
        if [arr[2],arr[3],arr[0],arr[1]] not in store:
            if (pos[0] != pos2[0] and pos[1] != pos2[1]) or (pos2[1]<s and pos2[0]<s and pos[0]>0 and pos[1]>0):
                print(pos+pos2)
                all_lines.append(pos+pos2)

print(all_lines)
print('\nLines: '+str(len(all_lines))+'\n')


#draw_canv.line(tuple(li),fill=palette['white'])
#draw_my_canvas.line(tuple(li),fill=palette['black'])

def draw_line (image_obj, stored_lines, brightness, iterations=0):
    """This Function Only Accepts square images"""
    
    #Add to iterations and print them
    iterations += 1
    print(iterations)
    
    #The image to work with
    pic = image_obj.copy()
    draw_pic = ImageDraw.Draw(pic,'RGBA')
    
    #Find darkest pixel
    darkest_pixel_image = pic.convert('L')
    darkest_pixel_list = list(darkest_pixel_image.getdata())
    darkest_pixel_min = min(darkest_pixel_list)
    #print(darkest_pixel_list)
    darkest_pixel_index = darkest_pixel_list.index(darkest_pixel_min)
    
    #Darkest pixel
    darkest_pixel_coords = (round(darkest_pixel_min%s),round((darkest_pixel_min-(darkest_pixel_min%s))/s))
    
    #Get the color of the pixel
    fixed_pix = pic.getpixel(darkest_pixel_coords)
    
    
    def get_score(image,image_copy):
        diff = ImageChops.difference(line_copy.convert('L'), image.convert('L'))
        score = numpy.mean([x for x in list(diff.getdata()) if x != 0])
        
        return score
    
    def get_valid_lines(stored_lines,darkest_pixel,image):
        #Valid lines
        valid_lines = []
         
        for line in stored_lines:
            print(line)
            #Check if it doesn't have an undefined slope
            if line[0]-line[2] != 0:
                #Get the slope of the line
                slope = (line[1]-line[3])/(line[0]-line[2])
                b_component = line[1]-slope*line[0]
                test_line = darkest_pixel[0]*slope+b_component
                
                #See if it is near to the selected pixel
                if test_line > darkest_pixel[1]-bound and test_line < darkest_pixel[1]+bound:
                    line_copy = pic.copy()
                    new_draw = ImageDraw.Draw(line_copy,'RGBA')
                    new_draw.line(tuple(line),fill=palette['white'])
                    
                    #See if the pixel has changed
                    if line_copy.getpixel(darkest_pixel) != fixed_pix:
                        score = get_score(pic,line_copy)
                        valid_lines.append([line,score])
                        
            #If it does...
            elif line[0] == darkest_pixel[0] and line[0]-line[2] == 0:
                #See if the point has changed
                line_copy = pic.copy()
                new_draw = ImageDraw.Draw(line_copy,'RGBA')
                new_draw.line(tuple(line),fill=palette['white'])
                
                score = get_score(pic,line_copy)
                valid_lines.append([line,score])
        
        
        return valid_lines
        
            
    start = time.time()
    valid_lines = get_valid_lines(stored_lines, darkest_pixel_coords, pic)
    for line in valid_lines:
        draw_pic.line(tuple(line[0]),fill=palette['white'])
    print(valid_lines)
    end = time.time()

    #sorted_lines = sorted(valid_lines, key=lambda e: e[1], reverse=True)
    
        
    
    print('Time it took to run: '+str(round(end - start))+' s')

draw_line(pic,all_lines,240)
