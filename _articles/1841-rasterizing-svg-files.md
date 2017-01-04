---
layout: graphics
category: graphics
title: Rasterizing SVG Files
permalink: /graphics/rasterizing-svg-files/
tags:
  - 184
  - 1
---

# Rasterizing SVG Files

<br />

> [Read the full writeup.](/graphics/1841)

<br />

In a broad sense, this project's **rasterizer** draws SVG files to the screen. It includes controls for antialiasing (via supersampling), transforms (scaling, translation, rotation), and switching between texture filtering methods.

<br />

_Rasterization_... the act of turning virtual objects into well-positioned, colored pixels on our displays. We begin by implementing the pixelation process for lines and triangles, since they can be synthesized into all other forms of geometric output. In both cases we essentially just need to figure out which pixels are part of the given line or triangle, and mark them in the framebuffer for coloring.

<br />

For lines we follow Bresenham's algorithm, which makes consistent single-unit strides in either a horizontal or vertical direction and varies progress along the other direction according to the input slope.

<br />

<img src="/images/part1.jpg" data-action="zoom" />

<br />

For triangles, we determine the bounding box from the vertex extremes, compute the barycentric coordinates of each point in the bounding box, and mark each point to be colored if all of its barycentric coordinates are between 0 and 1.

<br />

The triangle edges are antialiased through supersampling: we take multiple samples at different points within each pixel and set opacity to be the percentage of samples that are actually inside the triangle.

<br />

<img src="/images/test4_sr16.jpg" data-action="zoom" />

<br />

We also add support for basic affine transformations – applied below on our friend the golden robot – by providing the general matrices with which to multiply each collection of primitives.

<br />

<table><tr>
    <td style="text-align: center" width="50%">
        <img src="/images/robot.gif" data-action="zoom" />
    </td>
    <td style="text-align: center" width="50%">
        <img src="/images/test5_rotate.jpg" data-action="zoom" />
    </td>
</tr></table>

<br />

Finally, we enable our rasterizer to smoothly texture images onto arbitrary shapes by trilinearly interpolating colors from mipmaps.

<br />

<img src="/images/16_bilinear.jpg" data-action="zoom" />
