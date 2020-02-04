from PIL import Image, ImageFilter


img = Image.open('/home/didi/dev/u2020/17/astro.jpg')
converted_image = img.resize((400, 400))
converted_image.show()
# for keep aspect ratio
img.thumbnail((400, 400))
img.save('thambnail.jpg')
img.show()