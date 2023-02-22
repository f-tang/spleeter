import os
from argparse import ArgumentParser

import ffmpeg

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--path', type=str, help="Root directory of ouput and clean_vocals folder.")
    args = parser.parse_args()
    path = args.path
    if path is None:
        print("Please specify --path as the root directory")
        exit(0)

    output_path = os.path.join(path, "output")
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    for file in os.listdir(path):
        stem, ext = os.path.splitext(file)
        if ext == ".wav":
            src = os.path.join(path, file)
            dst = os.path.join(output_path, stem + "p%02d" + ext)
            os.system("ffmpeg -i {} -f segment -segment_time 15 -c copy {}".format(src, dst))
