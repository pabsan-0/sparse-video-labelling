#! /usr/bin/env python3

import cv2
import pathlib
import argparse


"""
gets a video file and dumps each frame as a png picture in an output dir
"""

parser = argparse.ArgumentParser()

parser.add_argument('-i','--video_path',  help="Path to the input video file",   type=str)
parser.add_argument('-o','--image_path',  help="Path to image output dis",       type=str, default="./")
parser.add_argument('-p','--prefix',      help="Prefix for output image files",  type=str, default="")
parser.add_argument('-d','--decimator',   help="Save only one every _d_ frames", type=int, default=1)
parser.add_argument('-s','--image_size',  help="Output image square resolution", type=int, default=1920)
parser.add_argument('-f','--first_frame', help="First frame to store",           type=int, default=0)
parser.add_argument('-l','--last_frame',  help="Last frame to store",            type=int, default=99999)

args = parser.parse_args()
assert(args.video_path and args.image_path)


if __name__ == "__main__":
    pathlib.Path(args.image_path).mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(args.video_path)
    total_n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count = 0

    print("    Converting video to frames... ")
    while(cap.isOpened()):

        ret, frame = cap.read()
        if ret == False:
            break

        if all([
            frame_count >= args.first_frame, 
            frame_count <= args.last_frame, 
            frame_count %  args.decimator == 0
            ]):
            frame = cv2.resize(frame, (args.image_size, args.image_size))
            cv2.imwrite(f"{args.image_path}/{args.prefix}{frame_count:05}.png", frame)

        frame_count += 1
        print(f"   Processing frame {frame_count}/{total_n_frames}\r", end="")

    cap.release()
    print("\n    Done!")

