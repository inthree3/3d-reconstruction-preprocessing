import os
import cv2
import numpy as np
file_path='E:/Desktop/COLMAP_cloth_test/inseon/mask_white'
file_names=os.listdir(file_path)

for name in file_names:
    print(name)
    img=cv2.imread(os.path.join(file_path,name))
    print(img)
    out = img.copy()
    out = np.sum(out,axis=-1)
    out = out>0.0
    cv2.imwrite(os.path.join(file_path,name),255*out)