import os

file_path='E:/Desktop/COLMAP_cloth_test/inseon/mask_white'
file_names=os.listdir(file_path)

i=0
for name in file_names:
    src=os.path.join(file_path, name)
    dst=str(i).zfill(6)+'.jpg.png'
    dst=os.path.join(file_path, dst)
    os.rename(src, dst)
    i+=1