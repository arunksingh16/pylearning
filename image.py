

from PIL import Image, ImageFilter
img = Image.open('/Users/arunkumarsingh/Desktop/mohnish-landge-BjEKmyBGl8g-unsplash.jpg')
print(img.mode)
print(img.format)
print(img.size)

# print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("/Users/arunkumarsingh/Desktop/x.png", 'png')
resize_img = img.resize((300,300))
resize_img.save("/Users/arunkumarsingh/Desktop/y.png", 'png')
