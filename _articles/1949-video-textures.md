---
layout: graphics
category: graphics
title: Video Textures
permalink: /graphics/video-textures/
tags:
  - 194
  - 9
---

# Video Textures

<br />

> [Read the full writeup.](/graphics/1948/#video-textures)

<br />

To create dynamically looping videos (aka **video textures**), we use SSD comparisons between proposed frame successors and actual frame successors in order to identify good transitions between temporal positions in a training video. We then reuse the content of the source video, probabilistically jumping between its frames in a way that (a) takes advantage of quality transitions and (b) avoids dead ends. We'll continue to write out these frames until we've created a video of desired (yet theoretically arbitrary) length.

<br />

In each of the below examples, the first video is the training source and the second is the program output.

<br />

<iframe width="100%" height="300px" src="https://www.youtube.com/embed/j-LUcIcMyds" frameborder="0" allowfullscreen></iframe>

<br />

<iframe width="100%" height="300px" src="https://www.youtube.com/embed/_ZnsskNBOXY" frameborder="0" allowfullscreen></iframe>

<br />

The following texture contains rare footage of a certain dark-furred lagomorph chewing on parsley.

<br />

<iframe width="100%" height="300px" src="https://www.youtube.com/embed/OGmGAxp6cjo" frameborder="0" allowfullscreen></iframe>

<br />

<iframe width="100%" height="300px" src="https://www.youtube.com/embed/wzz7A1OhfZw" frameborder="0" allowfullscreen></iframe>
