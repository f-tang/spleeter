import os
from argparse import ArgumentParser

src_file_prefix = {
    "car01": [],
    "car02": [],
    "car03": [],
    "car04": [],
    "car05": [],
    "phone01": [],
    "phone02": [],
    "phone03": [],
    "phone04": [],
    "special01": [],
    "special02": [],
    "special03": [],
}

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--path', type=str, help="Root directory of source files.")
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
        file_prefix = file.split('_')[0]
        if file_prefix in src_file_prefix:
            src = os.path.join(path, file)
            src_file_prefix[file_prefix].append(src)

    for (key, value) in src_file_prefix.items():
        input_str = ""
        stream_str = ""
        for i in range(len(value)):
            input_str += "-i {} ".format(value[i])
            stream_str += "[{}:0]".format(i)

        postfix = value[0].split('_')[-2:]
        dst = os.path.join(output_path, key + '_' + '_'.join(postfix))
        cmd = "ffmpeg {}-filter_complex {}concat=n={}:v=0:a=1[out] -map [out] {}".format(
            input_str, stream_str, len(value), dst
        )
        os.system(cmd)
        print("Output: {}".format(dst))
