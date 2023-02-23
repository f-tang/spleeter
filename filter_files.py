import os
from argparse import ArgumentParser

import ffmpeg

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--path', type=str, help="Root directory of audio files.")
    args = parser.parse_args()
    path = args.path
    if path is None:
        print("Please specify --path as the root directory")
        exit(0)

    output_path = os.path.join(path, "output")
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    file_list = []
    for file in os.listdir(path):
        stem, ext = os.path.splitext(file)
        if ext == ".wav":
            file_list.append(os.path.join(path, file))

    if len(file_list) > 0:
        src_str = " ".join(file_list)
        cmd = "python -m spleeter separate -p spleeter:2stems -o output {}".format(src_str)
        os.system(cmd)
