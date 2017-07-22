from PIL import Image, ImageOps, ImageDraw
import time

class Snap():
    def __init__ (self, image, n_of_points, bound, border):
        
        #Open image
        self.image = Image.open(str(image))
        
        #Number of points per side of the image (preferably a square)
        self.n_of_points = n_of_points
        
        #Range where lines fall into
        self.bound = bound
        
        #Border thickness
        self.border = border
        
        #Canvas
        self.canvas = Image.new("RGB", 
            (self.image.width + 2*border, self.image.width + 2*border), 
            (255,255,255,255)
            )

    def set_colors (self, colors):
        self.colors = colors
        
    def process_image(self):
        #Create borders
        self.snap = Image.new("RGB", 
            (self.image.width, self.image.width), (0,0,0,255))
            
        self.snap.paste(self.image)
        
        self.snap = ImageOps.expand(self.snap, self.border, 
            fill=(255,255,255,255))
            
        self.on_snap = ImageDraw.Draw(self.snap,'RGBA')
        
        self.on_canvas = ImageDraw.Draw(self.canvas,'RGBA')
        
    def get_all_positions(self):
        
        self.get_all_positions_start = time.time()
        self.store = []
        s = self.snap.width
        n = self.n_of_points
        
        for i in range(n):
            coor = s / (n - 1) * i
            st = [[coor, 0], [0, coor], [s, coor], [coor, s]]
            
            for ele in st:
                if ele not in self.store:
                    self.store.append(ele)
                    
        self.get_all_positions_end = time.time()
        
    def get_all_lines(self):
        self.get_all_lines_start = time.time()
        self.all_lines = []
        
        for pos in self.store:
            
            for pos2 in self.store:
                arr = pos+pos2
                
                if [arr[2],arr[3],arr[0],arr[1]] not in self.all_lines:
                  
                    if ((pos[0] != pos2[0] and pos[1] != pos2[1]) or 
                        (pos2[1]<self.snap.width and
                        pos2[0]<self.snap.width and 
                        pos[0]>0 and 
                        pos[1]>0)):
                        
                        self.all_lines.append(arr)
        
        self.get_all_lines_end = time.time()
        
    def print_data(self):
        #print(self.all_lines)
        print('\nPos: '+str(len(self.store)))
        print('Time it took: '
            +str(self.get_all_positions_end - 
            self.get_all_positions_start))
        
        print('\nLines: '+str(len(self.all_lines)))
        print('Time it took: '
            +str(self.get_all_lines_end - self.get_all_lines_start))
            
    def set_up(self):
        self.process_image()
        self.get_all_positions()
        self.get_all_lines()
        self.print_data()
