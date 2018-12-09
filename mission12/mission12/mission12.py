import os
from PIL import Image

class ImageFolder:
    def __init__(self, path):
        #create a dictionnary of the containing file of a sub-directorie
        self.__image_dico = {}
        for fil in os.scandir(path):
            if fil.is_dir():
                self.__image_dico[fil.name] = self.get_dir_files(os.path.join(path,fil))


    def get_dir_files(self, path):
        """
        Return all the file from a path as a list
        """
        file_lst = []
        for fil in os.scandir(path):
            if not fil.name.startswith('.') and fil.is_file():
                file_lst.append(fil.name)
        file_lst.sort()
        #the -1 represent the counter
        return [file_lst,0]

        
    def next(self, name):
        """
        Take care of the second element of the list in the dictionnary
        """
        #prevent the case when there is no sub-folder such that the dictionnary is empty
        if self.__image_dico == {}:
            raise ValueError("The dictionnary is empty, look the path or add sub-folder")
            return

        info_lst = self.__image_dico[name]
        #prevents the case when there is no elements in the folder
        if info_lst[0] == []:
            return "This folder does not contain any file"
        if info_lst[1] == len(info_lst[0]):
            info_lst[1] = 0
        img = info_lst[0][info_lst[1]]
        info_lst[1] += 1
        return name + '/' + img


    def images_dico(self):
        return self.__image_dico
    

def read_ascii(name):
    """
    Return a matrix of 
    """
    #TODO Meilleur implémentation, c'est pas très beau
    file = open(name,"r")
    picture_matrix = []
    char_lst = []
    for l in file:
        for c in l.strip("\n"):
            char_lst.append(c)
        picture_matrix.append(char_lst)
        if len(picture_matrix[0]) != len(char_lst):
            raise ValueError("All the line don't have the same length")
        char_lst = []
    return picture_matrix

def paths_matrix(ascii_matrix, img_fldr):
    path_matrix = []
    for l in ascii_matrix:
        new_lst = []
        for i in l:
            if i == ' ':
                new_lst.append(None)
            else:
                new_lst.append(img_fldr.next(str(i)))
        path_matrix.append(new_lst)
    return path_matrix


def img_builder(path_matrix, new_img_name, width, heigth, path):
    """
    Build the image followinf the path_matrix caneva,
    for some reason some space appears between the photos
    """
    size = (width, heigth)
    new_img_width = len(path_matrix[0]) * width
    new_img_heigth = len(path_matrix) * heigth
    x_pos = 0
    y_pos = 0

    new_img = Image.new("RGBA", (new_img_width, new_img_heigth))
    for l in path_matrix:
        x_pos = 0
        for pth in l:
            if pth != None:
                new_pth = os.path.join(path, pth)
                img = Image.open(new_pth)
                img.thumbnail(size)
                new_img.paste(img, (x_pos, y_pos))
            x_pos += width
        y_pos += 100
    new_img.save(new_img_name + ".png", "PNG")
    return


try:
    width_dim = int(input("Enter the width dimension in pixel: "))
    heigth_dim = int(input("Enter the heigth dimension in pixel: "))
    txt_file_name = input("Enter the file name: ")
    path = input("Enter the path of the images: ")
    new_img_name = input("Enter the name of the new image: ")
    imfFold = ImageFolder(path)
    ascii_matrix = read_ascii(txt_file_name)
    pth_mat = paths_matrix(ascii_matrix, imfFold)
    img_builder(pth_mat, new_img_name, width_dim, heigth_dim , path)

except:
    raise ValueError("Something went wrong with the initialisation. Have you entered correct values?")


"""

path = "/home/thetheos/Documents/Université/BAC1/INFO1/BAC1INFO1/mission12/mission12/photos"
imfFold = ImageFolder(path)
ascii_matrix = read_ascii("BAC1INFO1/mission12/mission12/img.txt")
pth_mat = paths_matrix(ascii_matrix, imfFold)
img_builder(pth_mat, "test", 100, 100 , path)



print(imfFold.images_dico())

print(imfFold.next("2"))

print(imfFold.next("2"))

print(imfFold.next("2"))


print(paths_matrix(ascii_matrix, imfFold))
"""

