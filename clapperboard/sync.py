from moviepy.editor import *
import sys
import os


def sync_clips(video_filename, audio_filename, video_start, audio_start, out_filename):
    video_clip = VideoFileClip(video_filename, audio=False).subclip(video_start)
    audio_clip = AudioFileClip(audio_filename).subclip(audio_start)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(out_filename, fps=25)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    video_filename, audio_filename, video_start, audio_start, out_filename = args
    video_filename = os.path.abspath(video_filename)
    audio_filename = os.path.abspath(audio_filename)
    video_start = float(video_start)
    audio_start = float(audio_start)
    out_filename = os.path.abspath(out_filename)
    sync_clips(video_filename, audio_filename, video_start, audio_start, out_filename)


if __name__ == '__main__':
    main()
