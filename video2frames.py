import cv2
vidcap = cv2.VideoCapture('C:/Users/owner/Desktop/COLMAP_cloth_test/cloth_video.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("C:/Users/owner/Desktop/COLMAP_cloth_test/cloth_video_frames/%06d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

print("finish! convert video to frame")