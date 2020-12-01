import sys
import os
from PIL import Image

# i want to take arguments in the bash command
# python3 jpgtopng.py folder1/ folder2/

source_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(source_folder):
    if '.jpg' in filename:
        img = Image.open(f'{source_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{output_folder}{clean_name}.png', 'png')

