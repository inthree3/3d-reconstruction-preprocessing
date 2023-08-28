from PIL import Image
import os

image_path="E:/Desktop/COLMAP_cloth_test/inseon/mask_white"
image_names=os.listdir(image_path)

os.chdir(image_path)

target=(720, 720)
for image in image_names:
    img=Image.open(image)
    img_resized=img.resize(target)
    img_resized.save(image)

