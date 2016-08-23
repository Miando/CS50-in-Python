with open('card.raw', 'rb') as f:
    jpgdata = f.read()
b=0
p=""
photo_name=000
list_of_photos=[]
while True:
    photo_name=photo_name+1
    a=jpgdata.find('\xff\xd8',b+1)
    b=jpgdata.find('\xff\xd8',a+1)
    photo=jpgdata[a:b]
    if photo in list_of_photos:
        break
    list_of_photos.append(photo)
    p=str(photo_name)+".jpg"
    w= open(p, 'wb')
    w.write(photo)
    w.close()
f.close()
