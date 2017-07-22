#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageChops, ImageOps
from snap import Snap
import math, time, numpy, random

palette = {'white': (255, 255, 255, 15), 'red': (255, 0, 0, 120),
           'black': (0, 0, 0, 15)}

my_pic = Snap('./testpictures/einstein.jpg', 50, 1, 5)
my_pic.set_up()

def get_pix_coords(image):

    # B&W

    darkest_pixel_image = image.convert('L')

    # Turn image into list

    darkest_pixel_list = list(darkest_pixel_image.getdata())

    # Darkest pixel

    darkest_pixel = sorted(darkest_pixel_list)

    darkest_pixel_index = darkest_pixel_list.index(darkest_pixel[0])

    return (round(darkest_pixel_index % darkest_pixel_image.width),
            round((darkest_pixel_index - darkest_pixel_index
            % darkest_pixel_image.width) / darkest_pixel_image.width))


def get_score(image, image_copy):

    diff = ImageChops.difference(image_copy.convert('L'),
                                 image.convert('L'))
    score = numpy.mean([x for x in list(diff.getdata()) if x != 0])

    return score


def get_valid_lines(
    stored_lines,
    darkest_pixel,
    image,
    bound,
    ):

    # Valid lines

    valid_lines = []

    # Get the color of the pixel

    fixed_pix = image.getpixel(darkest_pixel)

    for line in stored_lines:

        # Check if it doesn't have an undefined slope

        if line[0] - line[2] != 0:

            # Get the slope of the line

            slope = (line[1] - line[3]) / (line[0] - line[2])
            b_component = line[1] - slope * line[0]
            test_line = darkest_pixel[0] * slope + b_component

            # See if it is near to the selected pixel

            if test_line > darkest_pixel[1] - bound and test_line \
                < darkest_pixel[1] + bound:

                line_copy = image.copy()
                new_draw = ImageDraw.Draw(line_copy, 'RGBA')
                new_draw.line(tuple(line), fill=palette['white'])

                # See if the pixel has changed

                if line_copy.getpixel(darkest_pixel) != fixed_pix:
                    score = get_score(image, line_copy)
                    valid_lines.append([line, score])
        elif line[0] == darkest_pixel[0] and line[0] - line[2] == 0:

        # If it does...

            line_copy = image.copy()
            new_draw = ImageDraw.Draw(line_copy, 'RGBA')
            new_draw.line(tuple(line), fill=palette['white'])

            score = get_score(image, line_copy)
            valid_lines.append([line, score])

    return valid_lines

def sec_to_hour(seconds):
    hour = math.floor(seconds/3600)
    minutes = math.floor((seconds-3600*hour)/60)
    seconds_ = math.floor(seconds-hour*3600-minutes*60)
    
    print(str(hour)+'h : '+str(minutes)+'m : '+str(seconds_)+'s')

def draw_line(image_obj, brightness):
    """This Function Only Accepts square images"""

    # The image to work with

    pic = image_obj.snap.copy()

    # Get darkest pixel

    darkest_pixel_coords = get_pix_coords(pic.copy())
    
    start = time.time()

    # Get valid lines

    valid_lines = get_valid_lines(image_obj.all_lines,
                                  darkest_pixel_coords, pic.copy(),
                                  image_obj.bound)

    # Sorted lines by greatest average value

    sorted_lines = sorted(valid_lines, key=lambda e: e[1], reverse=True)
    
    print(len(sorted_lines))
    
    #Get line with the highest average
    
    image_obj.on_snap.line(tuple(sorted_lines[0][0]),
                           fill=palette['white'])
    image_obj.on_canvas.line(tuple(sorted_lines[0][0]),
                             fill=palette['black'])

    end = time.time()

    print ('Time it took to run: ' + str(end - start) + ' s')


start = time.time()
for i in range(8000):
    draw_line(my_pic, 240)
    my_pic.canvas.save('./results3/'+str(i)+'.jpg')
    print('#'+str(i))
end = time.time()
print( 'Time it took to run: ' + str(sec_to_hour(end - start)))

my_pic.canvas.show()
my_pic.snap.show()
my_pic.canvas.save('./results/einstein.jpg')


	
