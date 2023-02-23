import os
from argparse import ArgumentParser

videos = [
    "car01.mp4",
    "car02.mp4",
    "car03.mp4",
    "car04.mp4",
    "car05.mp4",
    "phone01.mp4",
    "phone02.mp4",
    "phone03.mp4",
    "phone04.mp4",
]

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--output', type=str, help="Root directory of output and clean_vocals folder.")
    parser.add_argument('--video_path', type=str, help="Root directory of video and clean_vocals folder.")
    parser.add_argument('--audio_path', type=str, help="Root directory of audio and clean_vocals folder.")
    args = parser.parse_args()
    output = args.output
    video_path = args.video_path
    audio_path = args.audio_path
    if video_path is None or audio_path is None:
        print("Please specify --video_path and --audio_path as the source directory")
        exit(0)

    if output is None:
        output = audio_path

    output_path = os.path.join(output, "output")
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    src_videos = {}
    for video_name in videos:
        stem, ext = os.path.splitext(video_name)
        src_videos[stem] = os.path.join(video_path, video_name)

    for audio_name in os.listdir(audio_path):
        stem, ext = os.path.splitext(audio_name)
        prefix = stem.split('_')[0]
        postfix = stem.split('_')[-2:]
        if prefix in src_videos:
            src_audio = os.path.join(audio_path, audio_name)
            dst = os.path.join(output_path, prefix + '_' + '_'.join(postfix) + '.mp4')
            cmd = "ffmpeg -i {} -i {} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 {}".format(
                src_videos[prefix], src_audio, dst
            )
            os.system(cmd)
            print("Output: {}".format(dst))
