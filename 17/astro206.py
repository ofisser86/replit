from PIL import Image, ImageFilter
from pathlib import Path
import sys


img_path = Path(sys.argv[1])
# files_in_basepath = basepath.iterdir()
dest = Path(sys.argv[2])
if not dest.exists():
    dest.mkdir()

img_list = img_path.glob('*.jpg')
#print(len(list(img_list))
for img in img_list:
    image = Image.open(img)
    resized_image = image.resize((400, 400))
    new_file_name = str(img).strip('.jpg')
    
    resized_image.save(f'{sys.argv[2]}/{new_file_name}_resized.png', 'png')
#resized_image.show()
# for keep aspect ratio
#img.thumbnail((400, 400))
#img.save('thambnail.jpg')
#img.show()