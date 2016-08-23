import PIL
from PIL import Image
r=5
img = Image.open('small.bmp')
img = img.resize(((img.size[0])*r,(img.size[1])*r), PIL.Image.ANTIALIAS)
img.save('sompic.bmp')
