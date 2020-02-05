import os, sys
from pathlib import Path
from PIL import Image

def right_slash(os_name):
    good_slash = '/'
    bad_slash = '\\'
    if os_name != 'linux':
        return bad_slash
    return good_slash 

try:
    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]
    slash = right_slash(sys.platform)
    # check if slash exist but does not cover all cases  
    if source_folder[-1] == slash and destination_folder[-1] == slash:
        source_folder = source_folder.strip()
        destination_folder = destination_folder.strip()
    else:
        source_folder += slash
        destination_folder += slash 

    # print(source_folder, destination_folder)
    jpg_list = list(Path(source_folder).glob('*.jpg'))
    
    # Chech if folder is empty
    if len(jpg_list) == 0:
        raise FileNotFoundError('There are no jpg files. Try another folder')
    


    # Create Path obj and chech if directory exist, if not create new
    dest_dir = Path(destination_folder)
    if not dest_dir.exists():
        dest_dir.mkdir() 

    for img in jpg_list:
        image = Image.open(img)
        converted_img = image.convert("L")
        
        clean_name = os.fspath(img).rstrip('.jpg').lstrip('Pokedex/')
        #clean_name = os.path.splitext(img)[0].split('Pokedex/')
        print(clean_name)
        converted_img.save(f'{dest_dir}/{clean_name}_converted.png', 'png')

    print("Converted!!!!!!!!!")
except IndexError as err:
    print(f'Add source and dest folders. Built in err is "{err}" ')

