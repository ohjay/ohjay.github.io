---
layout: graphics
category: graphics
title: Image Stitching
permalink: /graphics/image-stitching/
tags:
  - 194
  - 7
---

# Image Stitching

<br />

> [Read the full writeup.](/graphics/1947)

> [Read the writeup for part 1 only.](/graphics/1947a)

<br />

As a bit of a toy problem, we can rectify portions of an image by selecting the four corners of an item, marking their respective destinations, computing the homography matrix over the four pairs of matching points, and finally applying said matrix to the image as a whole. The example below has been rectified over the rightmost set of doors.

<br />

<table><tr>
    <td style="text-align: center" width="50%">
        <img src="/images/library.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="50%">
        <img src="/images/library_rectified.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

Of course, it doesn't have to be a rectangular target. We can warp into any shape we please, which means that we can easily <em>replace</em> certain regions of an image with other images' content. Take this collection of Hogwarts portraits, for instance:

<br />

<img src="/images/headmasters.jpg" data-action="zoom" />

<br />

We can replace two of the portrait subjects with [a video of Relno's Fox](https://www.youtube.com/watch?v=pixf8d_Od7M) through the following process:

<br />

<pre>
- Extract frames from the video using OpenCV.<br />
- Split the frames into two parts (one for each portrait).<br />
- Mark the positions of each of the two portraits' corners.<br />
- Warp and mask the target images into the portrait image.<br />
- Combine the resulting frames into a video.
</pre>

<br />

<div style="position: relative; padding-bottom: 70.80%"><iframe src="https://gfycat.com/ifr/CarefreeGentleBonobo" frameborder="0" scrolling="no" width="100%" height="100%" style="position: absolute; top: 0; left: 0" allowfullscreen></iframe></div>
<!-- <img class="gfyitem" data-id="CarefreeGentleBonobo" /> -->

<br />

For the main act, we stitch overlapping images into panoramas. This really just comes down to identifying corresponding feature points within pairs of images (either through manual selection or an automatic pipeline), warping images into each others' coordinate systems, and then blending pairs of images together in succession.

<br />

<table><tr>
    <td style="text-align: center" width="33.33%">
        <img src="/graphics/1947/images/indian1.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="33.33%">
        <img src="/graphics/1947/images/indian2.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="33.33%">
        <img src="/graphics/1947/images/indian3.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

<img src="/graphics/1947/images/indian_auto_cropped.jpg" data-action="zoom" />

<br />

We can do this automatically (i.e. given only a list of filepaths) by selectively warping only the images for which a sufficient number of matching points can be detected. The below panorama is the result of a fully automatic mosaicing process.

<br />

<table><tr>
    <td style="text-align: center" width="50%">
        <img src="/images/rain1.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="50%">
        <img src="/images/rain2.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

<img src="/graphics/1947/images/panorama0.jpg" data-action="zoom" />

<br />

To round it off, we're able to create 360&deg; panoramas through a similar (albeit simpler) cylindrical warping procedure.

<br />

<table><tr>
    <td style="text-align: center" width="11.11%">
        <img src="/images/almond1.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="11.11%">
        <img src="/images/almond2.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="11.11%">
        <img src="/images/almond3.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="11.11%">
        <img src="/images/almond4.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="11.11%">
        <img src="/images/almond5.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="11.11%">
        <img src="/images/almond6.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="11.11%">
        <img src="/images/almond7.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="11.11%">
        <img src="/images/almond8.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center" width="11.11%">
        <img src="/images/almond9.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

<link rel="stylesheet" href="https://cdn.pannellum.org/2.3/pannellum.css" />
<script type="text/javascript" src="https://cdn.pannellum.org/2.3/pannellum.js"></script>
<style>
    #almond-panorama { width: 99.5%; height: 220px; }
    pre {
        overflow-x: auto;
        white-space: pre-wrap;
        white-space: -moz-pre-wrap !important;
        word-wrap: break-word;
        white-space : normal;
    }
</style>
<div id="almond-panorama"></div>
<script>
pannellum.viewer('almond-panorama', {
    "type": "equirectangular",
    "minPitch": 0,
    "maxPitch": 0,
    "vaov": 60,
    "showZoomCtrl": false,
    "keyboardZoom": false,
    "mouseZoom": false,
    "showFullscreenCtrl": false,
    "panorama": "https://i.imgur.com/G8CX9lq.jpg"
});
</script>

<!-- Extra scripts -->
<!-- <script type="text/javascript" src="https://assets.gfycat.com/gfycat.js"></script> -->
