from PIL import Image, ImageFilter


img = Image.open('/home/didi/dev/u2020/17/image-playground/Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.DETAIL)
convered_img = img.convert('L')
box = (100, 100, 400, 400)
pika_face = convered_img.crop(box)
# convered_img.save('converted.png')
# filtered_img.save('filtered.png', 'png')
# filtered_img.show()
pika_face.show()

