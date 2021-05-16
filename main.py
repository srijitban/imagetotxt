import sys
from PIL import Image
image_path = sys.argv[0]
img = Image.open("Sour.jpg")
width, height = img.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio*new_width*0.55
img = img.resize((new_width,int(new_height)))
img = img.convert("L")
pixels = img.getdata()
chars = ["S","O","U","R","A","V"]
new_pixels = [chars[pixel//250] for pixel in pixels]
pixels = ''.join(new_pixels)
new_pixels_count= len(new_pixels)
ascii_image = [new_pixels[index:index+new_width] for index in range(0,new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
with open("ascii_image.txt",'w') as f:
    f.write(ascii_image)