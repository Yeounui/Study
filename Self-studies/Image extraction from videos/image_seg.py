import numpy as np
import cv2
import os

def image_extraction_from_video(load_video_file, save_images_dir):  # Source from book
    cap = cv2.VideoCapture(load_video_file)
    assert cap.isOpened(), 'No video file.'

    if not os.path.exists(save_images_dir):
        os.makedirs(save_images_dir)
    count = 0

    while True:
        ret, img = cap.read()
        if ret:
            imageName = os.path.join(save_images_dir, "frame%d.jpg" % count)
            
            cv2.imwrite(imageName, img)  # save frame as JPEG file
            print("saved a frame as " + imageName)
            
            if cv2.waitKey(10) & 0xFF == ord('e'):  # exit if Escape is hit
                break

            count += 1
        
        else:
            print('Each frame of %s is successfully extracted in the designated folder.'.load_image_file)
            break

    cap.release()

def image_grayscale_unification(load_image_file, save_image_file):
    img = cv2.imread(load_image_file, cv2.IMREAD_GRAYSCALE)
    assert img is not None, 'Failed reading image'
    
    ret, threshold_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # or cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC
    
    if ret:
        cv2.imwrite(save_image_file, threshold_img)
        print('Sucessfully save an unified image as ' + save_image_file)
    else:
        print('Failed image unification')