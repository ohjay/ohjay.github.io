---
layout: graphics
category: graphics
title: Single View Modeling
permalink: /graphics/single-view-modeling/
tags:
  - 194
  - 8
---

# Single View Modeling

<br />

> [Read the full writeup.](/graphics/1948)

<br />

This time around, the idea is that we'll take a one-point perspective image and reconstruct a 3D model (here an axis-aligned box) of its content. Our input is the image itself, a focal length, the coordinates of the back plane, and a vanishing point. With a bit of math, we can use this information to compute the depth of the scene. Then we can put together a 3D box, rectify each of the side images onto its walls, and tour its interior as we please.

<br />

<table>
    <tr>
        <td style="text-align: center" width="37.5%">
            <img src="/graphics/1948/images/frontal.jpg" data-action="zoom" />
        </td>
        <td style="text-align: center" width="62.5%">
            <img src="/graphics/1948/images/similartri.jpg" data-action="zoom" />
        </td>
    </tr>
</table>

<br />

Here's a video demonstrating the usage of our "tour into the picture" software. For those wondering, said software is controlled using both the keyboard and the mouse.

<br />

<iframe width="100%" height="300px" src="https://www.youtube.com/embed/NTMID-AhgBo" frameborder="0" allowfullscreen></iframe>

<br />

Below is a source image with the user-specified points overlayed onto it. From this depiction, it should be easy to see the vanishing lines, the back plane of our eventual model, and the other four planes to boot.

<br />

<img src="/images/st_jerome1.jpg" data-action="zoom" />

<br />

The next two figures contain novel views, captured whilst touring the inside of our box.

<br />

<img src="/images/st_jerome2.jpg" data-action="zoom" />

<br />

<img src="/images/st_jerome3.jpg" data-action="zoom" />

<br />

We continue with a few other examples. As you may or may not see, throne rooms seemed to provide decent geometry for our task.

<br />

<img src="/images/blue_throne0.jpg" data-action="zoom" />

<br />

<img src="/images/blue_throne1.jpg" data-action="zoom" />

<br />

<img src="/images/red_throne0.jpg" data-action="zoom" />

<br />

<img src="/images/red_throne1.jpg" data-action="zoom" />

<br />

<img src="/images/red_throne2.jpg" data-action="zoom" />

<br />

This final video is less of a serious one, and emerged originally through trial adjustment of the OpenGL viewing settings.

<br />

<iframe width="100%" height="300px" src="https://www.youtube.com/embed/4KkU5wncHcc" frameborder="0" allowfullscreen></iframe>
