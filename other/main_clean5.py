from PIL import Image, ImageDraw, ImageChops, ImageOps
from snap import Snap
import math, time, numpy

palette = {
    'white' : (255,255,255,15),
    'red' : (255,0,0,120),
    'black' : (0,0,0,15)
}

my_pic = Snap('geez.jpg', 50, 1, 5)
my_pic.set_up()
my_pic.set_colors(palette)
my_pic.snap.show()

def get_pix_coords(image):
    #B&W
    darkest_pixel_image = image.convert('L')
    
    #Turn image into list
    darkest_pixel_list = list(darkest_pixel_image.getdata())
    
    #Darkest pixel
    darkest_pixel = sorted(darkest_pixel_list)
    
    print('Min: ' + str(darkest_pixel[0]))
    
    darkest_pixel_index = darkest_pixel_list.index(darkest_pixel[0])
    
    return (
        round(darkest_pixel_index % darkest_pixel_image.width),
        round((darkest_pixel_index - 
        (darkest_pixel_index%darkest_pixel_image.width)) / 
        darkest_pixel_image.width)
        )
    
def get_score(image,image_copy):
    
    diff = ImageChops.difference(image_copy.convert('L'), image.convert('L'))
    score = numpy.mean([x for x in list(diff.getdata()) if x != 0])
    
    return score

def get_valid_lines(stored_lines,darkest_pixel,image,bound):
    
    #Valid lines
    valid_lines = []
    
    #Get the color of the pixel
    fixed_pix = image.getpixel(darkest_pixel)
    
    for line in stored_lines:
        
        #Check if it doesn't have an undefined slope
        if line[0]-line[2] != 0:
            print(line)
            #Get the slope of the line
            slope = (line[1]-line[3])/(line[0]-line[2])
            b_component = line[1]-slope*line[0]
            test_line = darkest_pixel[0]*slope+b_component
            
            #See if it is near to the selected pixel
            if (test_line > darkest_pixel[1]-bound 
                and test_line < darkest_pixel[1]+bound):
                    
                line_copy = image.copy()
                new_draw = ImageDraw.Draw(line_copy,'RGBA')
                new_draw.line(tuple(line),fill=palette['white'])
                
                #See if the pixel has changed
                if line_copy.getpixel(darkest_pixel) != fixed_pix:
                    score = get_score(image,line_copy)
                    valid_lines.append([line,score])
                    
        #If it does...
        elif line[0] == darkest_pixel[0] and line[0]-line[2] == 0:
            
            line_copy = image.copy()
            new_draw = ImageDraw.Draw(line_copy,'RGBA')
            new_draw.line(tuple(line),fill=palette['white'])
            
            score = get_score(image,line_copy)
            valid_lines.append([line,score])
    
    return valid_lines

def draw_line (image_obj, brightness):
    """This Function Only Accepts square images"""
    
    #The image to work with
    pic = image_obj.snap.copy()
    draw_pic = ImageDraw.Draw(pic,'RGBA')
    
    #Get darkest pixel
    darkest_pixel_coords = get_pix_coords(pic.copy())
    print('pic.width: '+str(pic.width))
    
    canv = Image.new("RGB", (pic.width, pic.width), (0,0,0,255))
    draw_canv = ImageDraw.Draw(canv,'RGBA')
    
    start = time.time()
    
    #Get valid lines
    valid_lines = get_valid_lines(
        image_obj.all_lines, darkest_pixel_coords, pic.copy(), image_obj.bound)
    
    #Sorted lines by greatest average value
    sorted_lines = sorted(valid_lines, key=lambda e: e[1], reverse=True)
    
    image_obj.on_snap.line(tuple(sorted_lines[0][0]),fill=palette['white'])
    image_obj.on_canvas.line(tuple(sorted_lines[0][0]),fill=palette['black'])
    
    #image_obj.snap.show()
    #image_obj.canvas.show()
    end = time.time()
    
    print(str(valid_lines)+'\n')
    print(str(sorted_lines)+'\n')
    print('Time it took to run: '+str(end - start)+' s')

start = time.time()
for i in range(1):
    draw_line(my_pic, 240)
end = time.time()
print('Time it took to run: '+str(end - start)+' s')

#my_pic.print_data()
my_pic.canvas.show()
my_pic.snap.show()
