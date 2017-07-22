from PIL import Image, ImageDraw, ImageChops, ImageOps
import math
import time
import numpy

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
    
    
