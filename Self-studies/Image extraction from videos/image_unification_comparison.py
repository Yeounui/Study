import cv2

load_image_file1 = 'C:\\Dataset\\BYJ_parasitevid_1\\frame0.jpg'
load_image_file2 = 'C:\\Dataset\\BYJ_parasitevid_2\\frame0.jpg'
img1 = cv2.imread(load_image_file1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(load_image_file2, cv2.IMREAD_GRAYSCALE)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
ret1, threshold_img1 = cv2.adaptiveThreshold(img1, 127, 255, cv2.THRESH_BINARY) # or cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC
ret2, threshold_img2 = cv2.adaptiveThreshold(img2, 127, 255, cv2.THRESH_BINARY)
if ret1 and ret2:
  cv2.imshow('thresh_img1', threshold_img1)
  cv2.imshow('thresh_img2', threshold_img2)
  cv2.waitKey(0)
  cv2.destroyAllWindows()