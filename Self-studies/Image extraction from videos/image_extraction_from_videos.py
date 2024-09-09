from image_seg import image_extraction_from_video
import os

video_files_dir = 'C:\\Dataset'

load_file_list = [os.path.join(video_files_dir, filename) for filename in os.listdir(video_files_dir)]
print(load_file_list)

for count in range(len(load_file_list)):
    load_video_file = load_file_list[count]
    save_images_dir = os.path.splitext(load_video_file)[0]
    image_extraction_from_video(load_video_file, save_images_dir)
