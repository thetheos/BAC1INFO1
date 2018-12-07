from PIL import Image
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path, "akwardsmilyu.png")
im = Image.open(image_path)
print(im.size)




"""
Question 2
"""
size = (100,100)
im.thumbnail(size)
im.save( "thumbnail", "PNG")

#Verifie que le thumbnail est bien de 100 * 100
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path, "thumbnail")
im = Image.open(image_path)
print(im.size)

"""
Qestion 3
"""
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path, "akwardsmilyu.png")
im1 = Image.open(image_path)
im2 = Image.open(image_path)
new_im = Image.new("RGBA", (400,200))
new_im.paste(im1)
new_im.paste(im1, (200,0)) #(200,0) = les coordonnées du coin supérieur droit. avec y dirigé vers le bas et x à droit
new_im.save("TWOSMILE", "PNG")
im2.paste(im1,(200,200))
print(new_im.size)