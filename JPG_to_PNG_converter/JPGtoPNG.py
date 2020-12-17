import sys
import os
from PIL import Image

# to get path and destination directory
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#it checks if destination folder exist. if not, it will create one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#conversion part
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')

print('JPG to PNG conversion successful!')

