from moviepy.editor import *
import moviepy
import sys
import os


def print_usage():
    print('Crops a video and (optionally) adds fadein/fadeout effects')
    print('')
    print('Usage:')
    print('\t')
    print('\tclapcrop filename out_filename start_seconds end_seconds [fadein_seconds fadeout_seconds]')
    print('\t')


def crop(filename, out_filename, start_seconds, end_seconds, fadein_seconds=None, fadeout_seconds=None):
    video_clip = VideoFileClip(filename).subclip(start_seconds, end_seconds)
    if fadein_seconds:
        video_clip = moviepy.video.fx.all.fadein(video_clip, fadein_seconds)
    if fadeout_seconds:
        video_clip = moviepy.video.fx.all.fadeout(video_clip, fadeout_seconds)
    video_clip.write_videofile(out_filename, fps=25)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if len(args) == 4:
        filename, out_filename, start_seconds, end_seconds = args
        fadein_seconds, fadeout_seconds = None, None
    elif len(args) == 6:
        filename, out_filename, start_seconds, end_seconds, fadein_seconds, fadeout_seconds = args
    else:
        print_usage()
        return
    filename = os.path.abspath(filename)
    out_filename = os.path.abspath(out_filename)
    start_seconds, end_seconds = float(start_seconds), float(end_seconds)
    fadein_seconds = float(fadein_seconds) if fadein_seconds else None
    fadeout_seconds = float(fadeout_seconds) if fadeout_seconds else None
    crop(filename, out_filename, start_seconds, end_seconds, fadein_seconds, fadeout_seconds)


if __name__ == '__main__':
    main()