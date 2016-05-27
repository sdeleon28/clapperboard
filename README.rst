************
Clapperboard
************

Want to record yourself playing over a backing track but want to use your
quality soundcard input instead of your camcorder's crappy audio? No problem,
we've got you covered!

Clapperboard is a thin wrapper around MoviePy that lets you synchronize your
video and audio by using a clapperboard-like technique. If you don't know what
I'm talking about, have a look at this post
-> http://www.learningguitarnow.com/blog/recording/how-to-record-a-video-while-playing-over-a-backing-track/

Instead of using a pricy UI based NLE, you can instead use this handy command
line script to sync your video and audio tracks.

Installation
============

Clone this repo and run ``pip install clapperboard``.

Usage
=====

Sync
----

Once you figure out the precise moment where you made your "clapperboard" sound
with your instrument for both tracks, you can replace your video's audio with
your real audio track by running ``clapsync``.

Syntax::

  clapsync audio_filename video_filename video_start audio_start out_filename

Example::

  clapsync guitar_solo.mp4 guitar_solo.wav 15.32 2.45 guitar_solo_sync.mp4

Crop
----

Once you've sync'd your video and audio tracks, you may want to remove the
part of the video where you signal with your "clapperboard" sound (apart from
the part of the video where you stretch yourself onto the keyboard to stop
recording). Clapperboard comes with another utility that lets you crop the video
from both sides and (optionally) add fadein/fadeout effects.

Syntax::

  clapcrop filename out_filename start_seconds end_seconds fadein_seconds fadeout_seconds

Example::

  clapcrop guitar_solo.mp4 guitar_solo.mp4 2 49 1 3

TODO
====

* PEP8 cleanup
* Command-line arguments cleanup