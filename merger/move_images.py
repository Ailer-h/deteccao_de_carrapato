#gonna read all labels in a folder and move corresponding images
#WORK IN PROGRESSS

import os

src: str = r"C:\Users\henri\OneDrive\Área de Trabalho\YOLO\deteccao_de_carrapato\merger\train\labels"
dst: str = r"C:\Users\henri\OneDrive\Área de Trabalho\YOLO\deteccao_de_carrapato\merger\train\images"
imgs: str = r"C:\Users\henri\OneDrive\Área de Trabalho\YOLO\deteccao_de_carrapato\merger\images_pool"

file_extension: str = ".jpg"

if __name__ == "__main__":
    for label in os.listdir(src):

        # Removes the id_tag of the file
        filename = "_".join(label.split("_")[1:])

        filename = ".".join((filename.split(".")[:-1])) + file_extension
        
        print("File exisits? ->", os.path.isfile(os.path.join(imgs, filename)))
