from PIL import Image
im = Image.open("clue.bmp") 

for x in xrange(im.size[0]):
    for y in xrange(im.size[1]):
        r,g,b = im.getpixel((x,y))
        if r==255 or g==246 :
            #print r,g,b
            b=255
            g=255
            r=255

        im.putpixel((x,y),(r,g,b))
im.save('verdict.bmp')
