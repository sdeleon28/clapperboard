************
Clapperboard
************

Want record yourself playing guitar with a camcorder while using the audio from
your audio interface? No problem, we've got you covered!

Clapperboard syncronizes your video an audio by using a clapperboard-like
technique. If you don't know what I'm talking about, have a look at this post
-> http://www.learningguitarnow.com/blog/recording/how-to-record-a-video-while-playing-over-a-backing-track/

Instead of using a pricy UI based NLE, you can instead use this handy command
line script to sync your video and audio tracks.

Installation
============

Clone this repo and run ``pip install clapperboard``.

Usage
=====

Syntax::

  clapsync audio_filename video_filename video_start audio_start out_filename

Example::

  clapsync guitar_solo.mp4 guitar_solo.wav 15.32 2.45 guitar_solo_sync.mp4
