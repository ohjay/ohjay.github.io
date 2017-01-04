---
layout: graphics
category: graphics
title: Seam Carving
permalink: /graphics/seam-carving/
tags:
  - 194
  - 4
---

# Seam Carving

<br />

> [Read the full writeup.](/graphics/1944)

<br />

**Seam carving** isn't a particularly complicated concept. Basically, we're removing unimportant "seams" of our images in order to adjust the size while also preserving the good stuff. We define the importance of each pixel as the pixel's gradient magnitude.

<br />

To determine the optimal <em>vertical</em> seam to remove, we follow the dynamic programming approach of computing the cumulative minimum "energy" (i.e. importance) of each pixel, and then backtracking from the least important entry in the bottommost row. Since the removal of one seam equates to the removal of one pixel from the total width, we repeat this process – identification and removal – until our image has the desired dimensions. Note that to reduce the height with only vertical seam removal, we can transpose the image, run the program as normal, and then transpose it back.

<br />

<table width="100%"><tr>
    <td style="text-align: center">
        <img src="/graphics/1944/images/cat.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center">
        <img src="/graphics/1944/images/cat_carved.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

<table width="100%"><tr>
    <td style="text-align: center">
        <img src="/graphics/1944/images/dubai2.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center">
        <img src="/graphics/1944/images/dubai2_carved.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

<table width="100%"><tr>
    <td style="text-align: center">
        <img src="/images/jellyfish.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center">
        <img src="/graphics/1944/images/jellyfish_hvcarved.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

<table width="100%"><tr>
    <td style="text-align: center">
        <img src="/graphics/1944/images/trolltunga.jpg" data-action="zoom" />
    </td>
    <td style="text-align: center">
        <img src="/graphics/1944/images/trolltunga_carved.jpg" data-action="zoom" />
    </td>
</tr></table>
