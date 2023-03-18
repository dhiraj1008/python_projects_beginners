# install the Pillow package (pip install Pillow)
# import pillow
# open up the image u need to resize
# print the current size of the image
# specify the new size of the image
# save the new sized image

from PIL import Image

def resize_image(s1,s2):
    image = Image.open("1640787215954.jpg")
    print(f"current size of image is :{image.size}")
    image1=image.resize((s1,s2))
    image1.save("resizedimg.jpeg")
    print("image resized and saved successfully")

s1=int(input("enter the row(width) size:\n"))
s2=int(input("enter the col(height) size:\n"))
resize_image(s1,s2)
