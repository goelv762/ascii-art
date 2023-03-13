from PIL import Image

im = Image.open('test.png', 'r')
pixel_values = list(im.getdata())
size_x, _ = im.size
im.close()

def rgb_to_char(rgb):
    
    chars = ['  ', '..', ',,', '::', 'ii', 'll', 'ww', 'WW']
    greyscale = sum(rgb) / len(rgb)
    return chars[int(round(((greyscale - 1) * (8 - 1) / (255 - 1) + 1), 0)) - 1]

ascii_image = [[]]

y = 0

for i in range(len(pixel_values)):
    ascii_image[y].append(rgb_to_char(pixel_values[i]))
    
    # next row
    if (i % size_x == 0 and i != 0):
        # moves down a line in text file
        ascii_image[y].append('\n')
        y += 1
        ascii_image.append([])
    
text_file = open('image.txt', 'w')

for row in ascii_image:
    text_file.writelines(row)
