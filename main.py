import cv2
import glob
import sys
import os

from PIL import Image


def convert_mp4_to_jpgs(path):
    if not os.path.exists('output'):
        os.mkdir('output')

    video_capture = cv2.VideoCapture(path)
    still_reading, image = video_capture.read()
    frame_count = 0
    while still_reading:
        file_path = f"output/frame_{frame_count:03d}.jpg"
        cv2.imwrite(file_path, image)

        still_reading, image = video_capture.read()
        frame_count += 1
    print("Convert from mp4 to jpgs ended successfully!")


def convert_jpgs_to_gif(output_folder):
    images = glob.glob(f"{output_folder}/*.jpg")
    images.sort()
    frames = [Image.open(image) for image in images]
    frames_one = frames[0]
    frames_one.save('converted_file.gif', format='GIF', append_images=frames,
                    save_all=True, duration=50, loop=0)
    print("Convert from jpgs to gif ended successfully!")


if __name__ == "__main__":
    your_file = sys.argv[1]
    convert_mp4_to_jpgs(your_file)
    convert_jpgs_to_gif('output')
